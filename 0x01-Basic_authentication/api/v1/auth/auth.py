#!/usr/bin/env python3
"""
A class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    A class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for a given path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current authenticated user
        """
        return None
