"""Ubiquitously useful utilities."""
from __future__ import annotations
import logging
import sys
from datetime import datetime

TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'


def format_time(dt: datetime) -> str:
    """Formats a datetime to ISO standard format."""
    return dt.strftime(TIMESTAMP_FORMAT)


def parse_time(dt: str) -> datetime:
    """Parses a datetime from an ISO standard format string."""
    return datetime.strptime(dt, TIMESTAMP_FORMAT)


class Result:
    """Models the possibility of generic and composable failure of multiple operations.
    """

    def __init__(self, successful: bool):
        self.successful = successful

    def bind(self, other: Result):
        """Monadically consumes another result, binding the final result.

        Any failure along an operation's chain is defined as a failure of the entire operation.

        Args:
            other: the Result to bind
        """
        if self.successful:
            self.successful = other.successful

    def ensure(self):
        """Ensures that the operation was successful, aborting the program if it was not.
        """
        if not self.successful:
            logging.error('One or more errors detected; aborting')
            sys.exit(255)

    @staticmethod
    def success() -> Result:
        """Creates a successful Result."""
        return Result(successful=True)

    @staticmethod
    def failure() -> Result:
        """Creates a failed Result."""
        return Result(successful=False)
