"""Analyze AWSets JSON."""
from __future__ import annotations

import json
from typing import Any

from classifyawsetsjsonbyregion.awsets import Awset, AwsetFilter
from classifyawsetsjsonbyregion.awsregion.classifier import Classifier
from classifyawsetsjsonbyregion.config import Config
from classifyawsetsjsonbyregion.csv import OutputCsv
from classifyawsetsjsonbyregion.filepath import FilePathCreator

CONFIG: Config = Config()


class AwsetsJsonAnalyzer:
    """To analyze AWSets JSON."""

    UTF8 = "utf-8"

    def __init__(self) -> None:
        CONFIG.load("config.yml")
        self.file_path_creator = FilePathCreator()
        self.classifier = Classifier(CONFIG.region_exclude)
        self.awset_filter = AwsetFilter(CONFIG.ignore_pattern)

    def analyze(self) -> None:
        awsets = json.loads(self.file_path_creator.path_resources_json.read_text(encoding=self.UTF8))
        awsets = [awset for awset in awsets if awset["Region"] not in CONFIG.region_exclude]
        self.file_path_creator.file_awsets_other_regions.write_text(json.dumps(awsets, indent=2), encoding=self.UTF8)
        for region_name, awsets_in_region in self.classifier.classify_by_region(awsets).items():
            self.analyze_each_region(region_name, awsets_in_region)

    def analyze_each_region(self, region_name: str, awsets: list[Awset]) -> None:
        """Analyzes AWSets in each region."""
        sorted_awsets = sorted(awsets, key=lambda x: (x["Type"], x["Name"], x["Tags"]))
        path_json = self.file_path_creator.create_path_json_per_region(region_name)
        path_json.write_text(json.dumps(sorted_awsets, indent=2), encoding=self.UTF8)
        output_csv = OutputCsv(self.file_path_creator.create_path_csv_per_region(region_name))
        with output_csv.writer() as writer:
            # Reason: Return values are None. pylint: disable=expression-not-assigned
            [writer.writerow(self.to_row(awset)) for awset in sorted_awsets if self.awset_filter.is_passed(awset)]

    @staticmethod
    def to_row(awset: Awset) -> list[Any]:
        return [awset["Type"], awset["Name"], awset["Tags"]]
