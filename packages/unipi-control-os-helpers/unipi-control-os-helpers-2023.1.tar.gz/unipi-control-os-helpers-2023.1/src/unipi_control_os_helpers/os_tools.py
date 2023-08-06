#!/usr/bin/python3
import tarfile
from pathlib import Path
from typing import Final
from rich import print as rich_print

import typer
from datetime import date

app = typer.Typer()
backup_app = typer.Typer()
install_app = typer.Typer()

app.add_typer(backup_app, name="backup", help="Backup Unipi Control.")
app.add_typer(install_app, name="install", help="Install Unipi Control.")


class PrintPrefix:
    DONE: Final[str] = "[bold][[/bold][bold green]DONE[/bold green][bold]][/bold]"
    ERROR: Final[str] = "[bold][[/bold][bold red]ERROR[/bold red][bold]][/bold]"
    SKIP: Final[str] = "[bold][[/bold][bold yellow]SKIP[/bold yellow][bold]][/bold]"


class BackupConstants:
    UNIPI_CONFIG_DIR: Path = Path("/usr/local/etc/unipi")
    BACKUP_DIR: Path = Path("/mnt/data/backup")


@backup_app.command("config", help="Backup Unipi Control configuration files.")
def backup_config() -> None:
    """Backup Unipi Control configuration."""
    try:
        if not BackupConstants.BACKUP_DIR.exists():
            BackupConstants.BACKUP_DIR.mkdir(parents=True)

        tar_file: Path = BackupConstants.BACKUP_DIR / f"config-{date.today()}.tar.gz"

        if tar_file.exists():
            rich_print(f"{PrintPrefix.SKIP} {tar_file.as_posix()} already exists!")
            raise typer.Exit(code=1)

        with tarfile.open(BackupConstants.BACKUP_DIR / f"config-{date.today()}.tar.gz", "x:gz") as tar:
            tar.add(BackupConstants.UNIPI_CONFIG_DIR, arcname=BackupConstants.UNIPI_CONFIG_DIR.name)
    except IOError as error:
        rich_print(f"{PrintPrefix.ERROR} {error.strerror}: '{error.filename}'")
        raise typer.Exit(code=1)

    rich_print(f"{PrintPrefix.DONE} {tar_file.as_posix()} created!")


if __name__ == "__main__":
    app()
