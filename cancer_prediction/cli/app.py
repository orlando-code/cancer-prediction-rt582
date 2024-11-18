"""
**Summary
The script defines a CLI with two commands:
__version__: Prints the version of the application.
run: Runs the Streamlit application by simulating the appropriate Streamlit CLI command.

**Usage
To print the version: python [app.py](http://_vscodecontentref_/17) __version__
To run the Streamlit app: python [app.py](http://_vscodecontentref_/18) run
This setup allows you to manage your application and its versioning through a simple CLI interface.


It's in its own folder since not everyone wants to use a CLI.

All CLI files are much of a muchness.
"""

import sys

import typer
from streamlit.web import cli as stcli

# from cancer_prediction import streamlit_app

app = typer.Typer()


@app.command()
def __version__():
    # Print the version of the app
    typer.echo("0.1.0")


@app.command()
def run():
    sys.argv = ["streamlit", "run", "cancer_prediction/streamlit_app.py"]
    sys.exit(stcli.main())


if __name__ == "__main__":
    app()
