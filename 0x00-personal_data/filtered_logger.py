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


PII_FIELDS = ("name", "email", "ssn", "ip", "user_agent")


def get_logger() -> logging.Logger:
    """Returns a cust configured logger obj"""
    user_data = logging.getLogger(__name__)
    user_data.propagate = False  # disable propagation to otger loggers
    user_data.setLevel(logging.INFO)  # logging no 20

    formatter = RedactingFormatter(PII_FIELDS)  # inst custom formatter

    stream_handler = logging.StreamHandler()  # create output handler
    stream_handler.setFormatter(formatter)  # set the formatter
    user_data.addHandler(stream_handler)  # register the handler on the logger

    return user_data
