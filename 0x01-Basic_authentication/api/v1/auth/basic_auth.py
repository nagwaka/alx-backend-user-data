#!/usr/bin/env python3
"""
A module to manage the API authentication
"""
from .auth import Auth
import re
import base64
import binascii


class BasicAuth(Auth):
    """
    Basic authentication class.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str,
            ) -> str:
        """
        Decodes a base64-encoded authorization header.
        """
        if type(base64_authorization_header) == str:
            try:
                response = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return response.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
