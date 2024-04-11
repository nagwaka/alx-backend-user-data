#!/usr/bin/env python3
"""
Filters logs
"""
import re
from typing import List


patterns = {
    'get': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """
    Obfuscates a log message
    """
    get, replace = (patterns["get"], patterns["replace"])
    return re.sub(get(fields, separator), replace(redaction), message)
