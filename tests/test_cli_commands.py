"""
CLI Command Extensions for Flask - Test Cases
"""
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from service.common.cli_commands import db_create


class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()

    @patch('service.common.cli_commands.db')
    def test_db_create(self, db_mock):
        """It should call the db-create command"""
        # Mock out db.create_all() and db.session.commit()
        db_mock.create_all = MagicMock()
        db_mock.session = MagicMock()
        db_mock.session.commit = MagicMock()

        # Force FLASK_APP to point to service/__init__.py
        with patch.dict(os.environ, {"FLASK_APP": "service.__init__:app"}, clear=True):
            result = self.runner.invoke(db_create)
            print("CLI OUTPUT:", result.output)
            self.assertEqual(result.exit_code, 0, f"Command failed: {result.output}")
