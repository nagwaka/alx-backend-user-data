#!/usr/bin/env python3
"""
Module for the API Session
"""
from uuid import uuid4
from flask import request

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    Class for Session authentication
    """
    pass
