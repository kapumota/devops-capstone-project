import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from service.common.cli_commands import db_create
from service.routes import app  # Import the Flask app
from service.common import status  # In case you need status codes

class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()

    @patch('service.common.cli_commands.db')
    def test_db_create(self, db_mock):
        """It should call the db-create command"""
        # Ensure our patched 'db' is a MagicMock
        db_mock.return_value = MagicMock()
        # Set FLASK_APP without clearing the whole environment
        with patch.dict(os.environ, {"FLASK_APP": "service:app"}):
            # Push an application context
            with app.app_context():
                # Invoke the command with standalone_mode=False to see real errors
                result = self.runner.invoke(db_create, [], standalone_mode=False)
        # Optionally, print result.output for debugging:
        # print("CLI output:", result.output)
        self.assertEqual(result.exit_code, 0)
