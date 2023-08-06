"""Model of AWSets."""
from __future__ import annotations

import re
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict  # pragma: no cover


class Awset(TypedDict):
    Region: str
    Type: str
    Name: str
    Tags: dict[str, str]


class AwsetFilter:
    """To filter AWSets data for specific investigation purpose."""

    def __init__(self, dict_ignore_pattern: dict[str, list[str]]) -> None:
        self.dict_ignore_pattern = dict_ignore_pattern

    def is_passed(self, awset: Awset) -> bool:
        """Filter AWSets data.

        Args:
            awset: AWSets data of target resource
        Returns:
            True: Target resource should be filtered
            False: Target resource should not be filtered
        """
        list_ignore_pattern = self.dict_ignore_pattern.get(awset["Type"])
        if not list_ignore_pattern:
            return True
        regex = "|".join(list_ignore_pattern)
        return not re.search(regex, awset["Name"])
