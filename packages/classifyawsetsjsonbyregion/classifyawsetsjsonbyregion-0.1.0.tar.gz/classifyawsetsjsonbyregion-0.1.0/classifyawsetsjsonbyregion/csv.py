"""Json to CSV."""
from contextlib import contextmanager, suppress
import csv
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

    import _csv

    # Reason: For type hinting.
    standard_csv_writer = _csv._writer  # noqa: SLF001  pylint: disable=protected-access,no-member


class OutputCsv:
    """To output AWSets data into CSV."""

    def __init__(self, path_csv: Path) -> None:
        self.path_csv = path_csv
        with suppress(FileNotFoundError):
            self.path_csv.unlink()

    @contextmanager
    def writer(self) -> "Generator[standard_csv_writer, None, None]":
        with self.path_csv.open("w", newline="") as csv_file_pointer:
            yield csv.writer(csv_file_pointer, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
