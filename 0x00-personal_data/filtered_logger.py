#!/usr/bin/env python3
"""
Filters logs
"""
import re
from typing import List
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records
        using filter_datum
        """
        message = super(RedactingFormatter, self).format(record)
        filtered_values = filter_datum(
                self.fields, self.REDACTION, message, self.SEPARATOR)
        return filtered_values
