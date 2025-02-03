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

    @patch('service.common.cli_commands.db_create.__globals__["init_db"]')
    def test_db_create(self, mock_init_db):
        """It should call the db-create command"""
        with patch.dict(os.environ, {"FLASK_APP": "service:app", "DATABASE_URI": "sqlite://"}):
            with app.app_context():
                result = self.runner.invoke(db_create, [], standalone_mode=False)

        mock_init_db.assert_called_once()             # or assert_called_once_with(app) / current_app
        self.assertEqual(result.exit_code, 0)
