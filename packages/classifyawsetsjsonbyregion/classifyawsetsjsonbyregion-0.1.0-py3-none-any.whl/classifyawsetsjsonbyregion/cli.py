"""Console script for classifyawsetsjsonbyregion."""
import sys

import click

from classifyawsetsjsonbyregion.analyzer import AwsetsJsonAnalyzer


@click.command()
def main() -> int:
    """Console script for classifyawsetsjsonbyregion."""
    AwsetsJsonAnalyzer().analyze()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
