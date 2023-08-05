import typer
from typer import Option

import tamp

app = typer.Typer(
    no_args_is_help=True, pretty_exceptions_enable=False, add_completion=False
)
# Add functions from other files like:
# app.command()(my_subcommand)


def version_callback(value: bool):
    if not value:
        return
    print(tamp.__version__)
    raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: bool = Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Print tamp version.",
    ),
):
    pass


def run_app(*args, **kwargs):
    app(*args, **kwargs)
