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

    @patch('service.models.db.create_all')
    def test_db_create(self, mock_create_all):
        """It should call the db-create command"""
        # mock_create_all will now patch the method as used by db_create
        with patch.dict(os.environ, {"FLASK_APP": "service:app"}):
            with app.app_context():
                # Using standalone_mode=False lets exceptions propagate
                result = self.runner.invoke(db_create, [], standalone_mode=False)
        # Check that create_all was indeed called
        mock_create_all.assert_called_once()
        self.assertEqual(result.exit_code, 0)
