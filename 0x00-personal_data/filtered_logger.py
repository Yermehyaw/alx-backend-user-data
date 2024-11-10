#!/usr/bin/env python3
"""
Logs, reads and filter user sensitive/non-sesnsitive data

Modules imported: typing, re, logging

"""
from typing import (
    List,
    Sequence,
)
import re
import logging


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """Returns an obfuscated log message"""
    for field in fields:
        pattern = rf'{field}=\s*(.*?){separator}'
        message = re.sub(pattern, f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = []) -> None:
        """Object initializer"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the logging for class objects"""
        return filter_datum(
            self.fields, self.REDACTION,
            record.getMessage(), self.SEPARATOR
        )
