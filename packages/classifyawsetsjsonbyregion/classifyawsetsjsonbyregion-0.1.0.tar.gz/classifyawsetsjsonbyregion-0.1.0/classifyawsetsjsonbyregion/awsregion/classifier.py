"""Classifies AWSets into each regions."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classifyawsetsjsonbyregion.awsets import Awset


REGIONS = {
    "us-east-1": "US East (N. Virginia)",
    "us-east-2": "US East (Ohio)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "ap-northeast-3": "Asia Pacific (Osaka)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ca-central-1": "Canada (Central)",
    "eu-central-1": "Europe (Frankfurt)",
    "eu-west-1": "Europe (Ireland)",
    "eu-west-2": "Europe (London)",
    "eu-west-3": "Europe (Paris)",
    "eu-north-1": "Europe (Stockholm)",
    "sa-east-1": "South America (São Paulo)",
    "aws-global": "global",
}


def create_classified_awsets_empty(regions_exclude: list[str]) -> dict[str, list[Awset]]:
    classified_awsets_empty: dict[str, list[Awset]] = {}
    for region_name in REGIONS:
        if region_name in regions_exclude:
            continue
        classified_awsets_empty[region_name] = []
    return classified_awsets_empty


class Classifier:
    """To report in each region."""

    def __init__(self, region_exclude: list[str]) -> None:
        self.classified_awsets = create_classified_awsets_empty(region_exclude)

    def classify_by_region(self, awsets: list[Awset]) -> dict[str, list[Awset]]:
        for awset in awsets:
            region = awset["Region"]
            self.classified_awsets[region].append(awset)
        return self.classified_awsets
