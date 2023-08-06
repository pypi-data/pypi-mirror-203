import unittest
from unittest.mock import patch

from gitlab_data_export.util import Result


class TestResult(unittest.TestCase):
    def test_success(self):
        result = Result.success()
        self.assertTrue(result.successful)

    def test_failure(self):
        result = Result.failure()
        self.assertFalse(result.successful)

    def test_bind(self):
        successful_result = Result.success()
        failed_result = Result.failure()

        failed_result.bind(successful_result)
        self.assertFalse(failed_result.successful)

        successful_result.bind(failed_result)
        self.assertFalse(successful_result.successful)

    @patch('sys.exit')
    @patch('logging.error')
    def test_ensure(self, mock_error, mock_exit):
        result = Result.success()
        result.ensure()
        mock_error.assert_not_called()
        mock_exit.assert_not_called()

        result = Result.failure()
        result.ensure()
        mock_error.assert_called_once()
        mock_exit.assert_called_once_with(255)
