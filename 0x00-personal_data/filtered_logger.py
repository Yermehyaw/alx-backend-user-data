
#!/usr/bin/env python3
"""
Logs, reads and filter user sensitive/non-sesnsitive data

Modules imported: typing, re

"""
from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """Returns an obfuscated log message"""
    for field in fields:
        pattern = rf'{field}=\s*(.*?){separator}'
        message = re.sub(pattern, field + '=' + redaction + separator, message)
    return message
