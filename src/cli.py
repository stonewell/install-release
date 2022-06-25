# pipi
import typer

# locals
from src.utils import rprint
from src.cli_interact import (
    GithubInfo,
    get as _get,
    upgrade as _upgrade,
)


def see_help(arg: str = ""):
    rprint(
        "This command required arguments, use "
        f"[yellow]{arg} --help[reset]"
        " to see them"
    )
    exit(1)


# cli debug type alias
__optionDebug = typer.Option(False, "-d", help="set debug mode.")

app = typer.Typer(help=f"release Installer")


@app.command()
def get(
    debug: bool = __optionDebug,
    url: str = typer.Argument(None, help="[URL] of github repository "),
):
    """
    | Install github release, cli tool
    """

    if url is None or url == "":
        see_help("get")
    repo = GithubInfo(url)
    _get(repo)


@app.command()
def upgrade(
    debug: bool = __optionDebug,
):
    """
    | Upgrade all github release, cli tools
    """
    _upgrade()


if __name__ == "__main__":
    app()
