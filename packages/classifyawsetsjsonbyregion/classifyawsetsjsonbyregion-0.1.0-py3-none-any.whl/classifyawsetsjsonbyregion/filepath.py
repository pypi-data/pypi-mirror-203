"""JSON per each regions."""
from pathlib import Path


class FilePathCreator:
    """To aggregate path to file."""

    DIRECTORY_INPUT = Path("input")
    DIRECTORY_INTERMEDIATE = Path("intermediate")
    DIRECTORY_OUTPUT = Path("output")

    def __init__(self) -> None:
        self.path_resources_json = self.DIRECTORY_INPUT / "awsets.json"
        output_file_name = f"{self.path_resources_json.stem}-other-regions.json"
        self.file_awsets_other_regions = self.DIRECTORY_INTERMEDIATE / output_file_name

    def create_path_json_per_region(self, regions_name: str) -> Path:
        return self.DIRECTORY_INTERMEDIATE / f"{self.file_awsets_other_regions.stem}-{regions_name}.json"

    def create_path_csv_per_region(self, region_name: str) -> Path:
        return self.DIRECTORY_OUTPUT / f"{self.file_awsets_other_regions.stem}-{region_name}.csv"
