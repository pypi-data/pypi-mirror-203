from __future__ import annotations

import logging
import typing as t

import requests

from .base import GlobusError
from .err_info import ErrorInfoContainer
from .warnings import warn_deprecated

log = logging.getLogger(__name__)


class GlobusAPIError(GlobusError):
    """
    Wraps errors returned by a REST API.

    :ivar http_status: HTTP status code (int)
    :ivar code: Error code from the API (str),
                or "Error" for unclassified errors
    :ivar message: Error message from the API. In general, this will be more
                   useful to developers, but there may be cases where it's
                   suitable for display to end users.
    """

    MESSAGE_FIELDS = ["message", "detail"]
    RECOGNIZED_AUTHZ_SCHEMES = ["bearer", "basic", "globus-goauthtoken"]

    def __init__(self, r: requests.Response, *args: t.Any, **kwargs: t.Any):
        self.http_status = r.status_code
        # defaults, may be rewritten during parsing
        self.code = "Error"
        self.message = r.text

        self._info: ErrorInfoContainer | None = None
        self._underlying_response = r
        self._parse_response()
        super().__init__(*self._get_args())

    @property
    def http_reason(self) -> str:
        """
        The HTTP reason string from the response.

        This is the part of the status line after the status code, and typically is a
        string description of the status. If the status line is
        ``HTTP/1.1 404 Not Found``, then this is the string ``"Not Found"``.
        """
        return self._underlying_response.reason

    @property
    def headers(self) -> t.Mapping[str, str]:
        """
        The HTTP response headers as a case-insensitive mapping.

        For example, ``headers["Content-Length"]`` and ``headers["content-length"]`` are
        treated as equivalent.
        """
        return self._underlying_response.headers

    @property
    def content_type(self) -> str | None:
        return self.headers.get("Content-Type")

    def _json_content_type(self) -> bool:
        r = self._underlying_response
        return "Content-Type" in r.headers and (
            "application/json" in r.headers["Content-Type"]
        )

    @property
    def raw_json(self) -> dict[str, t.Any] | None:
        """
        Get the verbatim error message received from a Globus API, interpreted
        as JSON data

        If the body cannot be loaded as JSON, this is None
        """
        r = self._underlying_response
        if not self._json_content_type():
            return None

        try:
            # technically, this could be a non-dict JSON type, like a list or string
            # but in those cases the user can just cast -- the "normal" case is a dict
            return t.cast(t.Dict[str, t.Any], r.json())
        except ValueError:
            log.error(
                "Error body could not be JSON decoded! "
                "This means the Content-Type is wrong, or the "
                "body is malformed!"
            )
            return None

    @property
    def text(self) -> str:
        """
        Get the verbatim error message received from a Globus API as a *string*
        """
        return self._underlying_response.text

    @property
    def raw_text(self) -> str:
        """
        Deprecated alias of the ``text`` property.
        """
        warn_deprecated(
            "The 'raw_text' property of GlobusAPIError objects is deprecated. "
            "Use the 'text' property instead."
        )
        return self.text

    @property
    def binary_content(self) -> bytes:
        """
        The error message received from a Globus API in bytes.
        """
        return self._underlying_response.content

    @property
    def info(self) -> ErrorInfoContainer:
        """
        An ``ErrorInfoContainer`` with parsed error data. The ``info`` of an error is
        guaranteed to be present, but all of its contents may be falsey if the error
        could not be parsed.
        """
        if self._info is None:
            rawjson = self.raw_json
            json_data = rawjson if isinstance(rawjson, dict) else None
            self._info = ErrorInfoContainer(json_data)
        return self._info

    def _get_request_authorization_scheme(self) -> str | None:
        try:
            authz_h = self._underlying_response.request.headers["Authorization"]
            authz_scheme = authz_h.split()[0]
            if authz_scheme.lower() in self.RECOGNIZED_AUTHZ_SCHEMES:
                return authz_scheme
        except (IndexError, KeyError):
            pass
        return None

    def _get_args(self) -> list[t.Any]:
        """
        Get arguments to pass to the Exception base class. These args are
        displayed in stack traces.
        """
        return [
            self._underlying_response.request.method,
            self._underlying_response.url,
            self._get_request_authorization_scheme(),
            self.http_status,
            self.code,
            # if the message is "", try using response reason
            # for details on these, and some examples, see
            #   https://datatracker.ietf.org/doc/html/rfc7231#section-6.1
            self.message or self._underlying_response.reason,
        ]

    def _parse_response(self) -> None:
        """
        This is an intermediate step between 'raw_json' (loading bare JSON data)
        and the "real" parsing method, '_load_from_json'

        _parse_response() pulls the JSON body and does the following:
        - if the data is not a dict, ensure _load_from_json is not called (so it only
          gets called on dict data)
        - if the data contains an 'errors' array, pull out the first error document and
          pass that to _load_from_json()
        - log a warning on non-dict JSON data
        """
        json_data = self.raw_json
        if json_data is None:
            log.debug("Error body was not parsed as JSON")
            return
        if not isinstance(json_data, dict):
            log.warning(  # type: ignore[unreachable]
                "Error body could not be parsed as JSON because it was not a dict"
            )
            return

        # if there appears to be a list of errors in the response data, grab the
        # first error from that list for parsing
        # this is only done if we determine that
        # - 'errors' is present and is a non-empty list
        # - 'errors[0]' is a dict
        #
        # this gracefully handles other uses of the key 'errors', e.g. as an int:
        #   {"message": "foo", "errors": 6}
        if (
            isinstance(json_data.get("errors"), list)
            and len(json_data["errors"]) > 0
            and isinstance(json_data["errors"][0], dict)
        ):
            # log a warning only when there is more than one error in the list
            # if an API sends back an error of the form
            #   {"errors": [{"foo": "bar"}]}
            # then the envelope doesn't matter and there's only one error to parse
            if len(json_data["errors"]) != 1:
                log.warning(
                    "Doing JSON load of error response with multiple "
                    "errors. Exception data will only include the "
                    "first error, but there are really %d errors",
                    len(json_data["errors"]),
                )
            # try to grab the first error in the list, but also check
            # if it isn't a dict
            json_data = json_data["errors"][0]
        self._load_from_json(json_data)

    def _load_from_json(self, data: dict[str, t.Any]) -> None:
        # rewrite 'code' if present and correct type
        if isinstance(data.get("code"), str):
            self.code = data["code"]

        for f in self.MESSAGE_FIELDS:
            if isinstance(data.get(f), str):
                log.debug("Loaded message from '%s' field", f)
                self.message = data[f]
                break
        else:
            log.debug("No message found in parsed error body")
