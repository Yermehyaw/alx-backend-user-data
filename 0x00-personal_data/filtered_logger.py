#!/usr/bin/env python3
"""
Logs, reads and filter user sensitive/non-sesnsitive data

Modules imported: typing, re

"""
from typing import List
from re import sub


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """Returns an obfuscated log message"""
    pattern = rf'({"|".join(fields)})=\s*(.*?){separator}'
    return sub(pattern, rf'\1={redaction}{separator}', message)
