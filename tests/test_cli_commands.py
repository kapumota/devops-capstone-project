import os
from unittest import TestCase
from unittest.mock import patch
from click.testing import CliRunner
from service.common.cli_commands import db_create
from service.routes import app

class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()

    @patch('service.common.cli_commands.db.create_all')
    def test_db_create(self, mock_create_all):
        """It should call the db-create command"""
        # When called, mock_create_all will do nothing (i.e. succeed)
        with patch.dict(os.environ, {"FLASK_APP": "service:app"}):
            with app.app_context():
                # Use standalone_mode=False so that exceptions are re‑raised
                result = self.runner.invoke(db_create, [], standalone_mode=False)
        # Ensure the command actually called db.create_all()
        mock_create_all.assert_called_once()
        self.assertEqual(result.exit_code, 0)
