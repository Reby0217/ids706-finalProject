import importlib

import api_generator.manager as manager
import click
from apps.config import API_GENERATOR
from flask.cli import with_appcontext


@click.command(name="gen_api")
@with_appcontext
def gen_api():
    for model in API_GENERATOR.values():
        try:
            models = importlib.import_module("apps.models")
            ModelClass = getattr(models, model)
            ModelClass.query.all()
        except Exception as e:
            print(f"Generation API failed because: {str(e)}")
            return

    try:
        manager.generate_forms_file()
        manager.generate_routes_file()
        print("APIs have been generated successfully.")
    except Exception as e:
        print(f"Generation API failed because: {str(e)}")
