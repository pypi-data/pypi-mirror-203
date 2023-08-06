"""
This module defines Exception classes used by Especifico to generate a proper response.
"""
from http import HTTPStatus

from jsonschema.exceptions import ValidationError
from werkzeug.exceptions import Forbidden, Unauthorized


class EspecificoException(Exception):
    pass


class ProblemException(EspecificoException):
    def __init__(
        self,
        status=HTTPStatus.BAD_REQUEST,
        title=HTTPStatus.BAD_REQUEST.phrase,
        detail=None,
        type=None,
        instance=None,
        headers=None,
        ext=None,
    ):
        """
        This exception holds arguments that are going to be passed to the
        `especifico.problem` function to generate a proper response.
        """
        self.status = status
        self.title = title
        self.detail = detail
        self.type = type
        self.instance = instance
        self.headers = headers
        self.ext = ext


class ResolverError(LookupError):
    def __init__(self, reason="Unknown reason", exc_info=None):
        """
        :param reason: Reason why the resolver failed.
        :type reason: str
        :param exc_info: If specified, gives details of the original exception
            as returned by sys.exc_info()
        :type exc_info: tuple | None
        """
        self.reason = reason
        self.exc_info = exc_info

    def __str__(self):  # pragma: no cover
        return f"<ResolverError: {self.reason}>"

    def __repr__(self):  # pragma: no cover
        return f"<ResolverError: {self.reason}>"


class InvalidSpecification(EspecificoException, ValidationError):
    pass


class NonConformingResponse(ProblemException):
    def __init__(self, reason="Unknown Reason", message=None, type=None):
        """
        :param reason: Reason why the response did not conform to the specification
        :type reason: str
        """
        super().__init__(status=500, title=reason, detail=message, type=type)
        self.reason = reason
        self.message = message

    def __str__(self):  # pragma: no cover
        return f"<NonConformingResponse: {self.reason}>"

    def __repr__(self):  # pragma: no cover
        return f"<NonConformingResponse: {self.reason}>"


class AuthenticationProblem(ProblemException):
    def __init__(self, status, title, detail):
        super().__init__(status=status, title=title, detail=detail)


class ResolverProblem(ProblemException):
    def __init__(self, status, title, detail):
        super().__init__(status=status, title=title, detail=detail)


class BadRequestProblem(ProblemException):
    def __init__(self, detail=None):
        super().__init__(
            status=HTTPStatus.BAD_REQUEST,
            title=HTTPStatus.BAD_REQUEST.phrase,
            detail=detail,
        )


class UnsupportedMediaTypeProblem(ProblemException):
    def __init__(self, detail=None):
        super().__init__(
            type="/errors/UnsupportedMediaType",
            status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
            title=HTTPStatus.UNSUPPORTED_MEDIA_TYPE.phrase,
            detail=detail,
        )


class NonConformingResponseBody(NonConformingResponse):
    def __init__(self, message, reason="Response body does not conform to specification"):
        super().__init__(
            type="/errors/NonConformingResponseBody",
            reason=reason,
            message=message,
        )


class NonConformingResponseHeaders(NonConformingResponse):
    def __init__(self, message, reason="Response headers do not conform to specification"):
        super().__init__(
            type="/errors/NonConformingResponseHeaders",
            reason=reason,
            message=message,
        )


class OAuthProblem(Unauthorized):
    pass


class OAuthResponseProblem(OAuthProblem):
    def __init__(self, token_response, **kwargs):
        self.token_response = token_response
        super().__init__(**kwargs)


class OAuthScopeProblem(Forbidden):
    def __init__(self, token_scopes, required_scopes, **kwargs):
        self.required_scopes = required_scopes
        self.token_scopes = token_scopes

        super().__init__(**kwargs)


class ExtraParameterProblem(ProblemException):
    def __init__(self, formdata_parameters, query_parameters, detail=None, **kwargs):
        self.extra_formdata = formdata_parameters
        self.extra_query = query_parameters

        # This keep backwards compatibility with the old returns
        if detail is None:
            if self.extra_query:
                detail = "Extra query parameter%s %s not in spec" % \
                    ("s" if len(self.extra_query) > 1 else "", ", ".join(self.extra_query))
            elif self.extra_formdata:
                detail = "Extra formData parameter%s %s not in spec" % \
                    ("s" if len(self.extra_formdata) > 1 else "", ", ".join(self.extra_formdata))

        super().__init__(type="/errors/ExtraParameter", detail=detail, **kwargs)
