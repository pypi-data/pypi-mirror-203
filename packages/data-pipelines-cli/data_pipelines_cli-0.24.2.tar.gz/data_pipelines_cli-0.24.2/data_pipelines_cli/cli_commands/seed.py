import click

from ..config_generation import get_profiles_dir_build_path
from ..dbt_utils import run_dbt_command
from .compile import compile_project


def seed(env: str) -> None:
    """
    Run the project on the local machine.

    :param env: Name of the environment
    :type env: str
    """
    compile_project(env)
    profiles_path = get_profiles_dir_build_path(env)
    run_dbt_command(("seed",), env, profiles_path)


@click.command(name="seed", help="Run 'dbt seed'")
@click.option(
    "--env",
    default="local",
    type=str,
    show_default=True,
    help="Name of the environment",
)
def seed_command(env: str) -> None:
    seed(env)
