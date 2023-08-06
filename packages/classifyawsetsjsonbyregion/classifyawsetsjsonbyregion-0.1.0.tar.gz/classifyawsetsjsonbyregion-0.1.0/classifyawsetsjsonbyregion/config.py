"""Configurations."""
from dataclasses import dataclass
from typing import Dict, List

from yamldataclassconfig import YamlDataClassConfig


@dataclass
class Config(YamlDataClassConfig):
    region_exclude: List[str] = None  # type: ignore[assignment]
    ignore_pattern: Dict[str, List[str]] = None  # type: ignore[assignment]
