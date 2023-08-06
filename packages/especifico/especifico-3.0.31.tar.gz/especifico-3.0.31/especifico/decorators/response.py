"""
This module defines a view function decorator to validate its responses.
"""

import asyncio
import functools
import logging

from jsonschema import ValidationError

from .decorator import BaseDecorator
from .validation import ResponseBodyValidator
from ..exceptions import (NonConformingResponseBody,
                          NonConformingResponseHeaders)
from ..utils import all_json, has_coroutine

logger = logging.getLogger("especifico.decorators.response")


class ResponseValidator(BaseDecorator):
    def __init__(self, operation, mimetype, validator=None, ref_resolver_store=None):
        """
        :type operation: Operation
        :type mimetype: str
        :param validator: Validator class that should be used to validate passed data
                          against API schema.
        :type validator: jsonschema.IValidator
        """
        self.operation = operation
        self.mimetype = mimetype
        self.validator = validator
        self._ref_resolver_store = ref_resolver_store

    def validate_response(self, data, status_code, headers, url):
        """
        Validates the Response object based on what has been declared in the specification.
        Ensures the response body matches the declared schema.
        :type data: dict
        :type status_code: int
        :type headers: dict
        :rtype bool | None
        """
        # check against returned header, fall back to expected mimetype
        content_type = headers.get("Content-Type", self.mimetype)
        content_type = content_type.rsplit(";", 1)[0]  # remove things like utf8 metadata

        response_definition = self.operation.response_definition(str(status_code), content_type)
        response_schema = self.operation.response_schema(str(status_code), content_type)

        if self.is_json_schema_compatible(response_schema, content_type):
            v = ResponseBodyValidator(
                response_schema,
                validator=self.validator,
                ref_resolver_store=self._ref_resolver_store,
            )
            try:
                data = self.operation.json_loads(data)
            except ValueError as e:
                if content_type != "text/plain":
                    raise NonConformingResponseBody(message=str(e)) from e
                elif isinstance(data, bytes):
                    try:
                        data = data.decode("utf-8")
                    except UnicodeDecodeError as e:
                        raise NonConformingResponseBody(message=str(e)) from None
            try:
                v.validate_schema(data, url)
            except ValidationError as e:
                raise NonConformingResponseBody(message=str(e)) from e

        if response_definition and response_definition.get("headers"):
            required_header_keys = {
                k
                for (k, v) in response_definition.get("headers").items()
                if v.get("required", False)
            }
            header_keys = set(headers.keys())
            missing_keys = required_header_keys - header_keys
            if missing_keys:
                pretty_list = ", ".join(missing_keys)
                msg = f"Keys in header don't match response specification. " \
                      f"Difference: {pretty_list}"
                raise NonConformingResponseHeaders(message=msg)
        return True

    def is_json_schema_compatible(self, response_schema: dict, content_type: str) -> bool:
        """
        Verify if the specified operation responses are JSON schema
        compatible.

        All operations that specify a JSON schema and have content
        type "application/json" or "text/plain" can be validated using
        json_schema package.
        """
        if not response_schema:
            return False
        return all_json([content_type]) or content_type == "text/plain"

    def __call__(self, function):
        """
        :type function: types.FunctionType
        :rtype: types.FunctionType
        """

        def _wrapper(request, response):
            especifico_response = self.operation.api.get_especifico_response(
                response, self.mimetype,
            )
            if not especifico_response.is_streamed:
                self.validate_response(
                    especifico_response.body,
                    especifico_response.status_code,
                    especifico_response.headers,
                    request.url,
                )
            else:
                logger.warning("Skipping response validation for streamed response.")

            return response

        if has_coroutine(function):

            @functools.wraps(function)
            async def wrapper(request):
                response = function(request)
                while asyncio.iscoroutine(response):
                    response = await response

                return _wrapper(request, response)

        else:  # pragma: no cover

            @functools.wraps(function)
            def wrapper(request):
                response = function(request)
                return _wrapper(request, response)

        return wrapper

    def __repr__(self):
        """
        :rtype: str
        """
        return "<ResponseValidator>"  # pragma: no cover
