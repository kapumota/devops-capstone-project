import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from service.common.cli_commands import db_create
from service.routes import app  # Import the Flask app

class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()

    @patch('service.common.cli_commands.db')
    def test_db_create(self, db_mock):
        """It should call the db-create command"""
        # Create a fake db object with create_all() that returns None
        fake_db = MagicMock()
        fake_db.create_all.return_value = None
        db_mock.return_value = fake_db

        # Set FLASK_APP in the environment without clearing it
        with patch.dict(os.environ, {"FLASK_APP": "service:app"}):
            # Push an application context so the CLI command can use the Flask app
            with app.app_context():
                # Use standalone_mode=False so that exceptions propagate
                result = self.runner.invoke(db_create, [], standalone_mode=False)

        # Optionally, you can print exception details for debugging:
        # print("Exception:", result.exception)

        self.assertEqual(result.exit_code, 0)
