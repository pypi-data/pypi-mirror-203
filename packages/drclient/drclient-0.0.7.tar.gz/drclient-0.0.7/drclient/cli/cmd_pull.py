from pathlib import Path

import typer

from ..image import pull_image


def pull(
    image_name: str = typer.Argument(..., help="The name of the image"),
    tar_file: Path = typer.Option(
        None, "-t", "--tar-file", help="Output to a tar.gz file"
    ),
    squafshfs_file: Path = typer.Option(
        None, "-s", "--squashfs-file", help="Output to a .sqfs file"
    ),
    output_directory: Path = typer.Option(
        None, "-d", "--output-directory", help="Output to a directory"
    ),
):
    """
    Pull image from a docker registry
    """
    pull_image(image_name, output_directory, tar_file, squafshfs_file)
