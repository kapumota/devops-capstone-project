"""
CLI Command Extensions for Flask
"""
import click
from flask.cli import with_appcontext
from service.models import db

@click.command("db-create")
@with_appcontext
def db_create():
    """Creates database tables"""
    click.echo("Creating database tables...")
    db.create_all()
    db.session.commit()
    click.echo("Created!")
