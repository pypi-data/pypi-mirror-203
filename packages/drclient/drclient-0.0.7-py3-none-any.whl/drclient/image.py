import atexit
import os
import shutil
import tarfile
from pathlib import Path
from subprocess import getstatusoutput
from tempfile import mkdtemp

import typer

from .registry import DockerRegistryClient
from .threaded_pull import pull_layers_in_threads
from .view.info import sizeof_fmt

DEFAULT_REGISTRY = os.environ.get("DOCKER_REGISTRY", "registry-1.docker.io")


def pull_image(
    image_url: str, output_directory=None, tar_file=None, squashfs_file=None
):
    """
    Pull image from a docker registry
    """
    is_tmp_output_directory = False
    registry, repository, tag = parse_image_url(image_url)
    source_reference = f"{registry}/{repository}:{tag}"

    drc = DockerRegistryClient(registry)
    drc.authenticate()
    manifest = drc.get_manifest(repository, tag)
    layers = manifest["layers"]
    local_image_name = f"{repository}:{tag}"
    total_size = sum([layer["size"] for layer in layers])
    print(
        f"Pulling {len(layers)} layer(s) [{sizeof_fmt(total_size)}] "
        f"for image {source_reference} to local image {local_image_name}"
    )

    if output_directory is None:
        output_directory = mkdtemp()
        if tar_file or squashfs_file:
            is_tmp_output_directory = True
            atexit.register(shutil.rmtree, output_directory)
    else:
        print(output_directory)
        if not output_directory.exists():
            output_directory.mkdir(parents=True)
        else:
            if not output_directory.is_dir():
                raise typer.BadParameter(
                    f"Output directory {output_directory} is not a directory"
                )
            os.scandir(output_directory)
            if any(os.scandir(output_directory)):
                raise typer.BadParameter(
                    f"Output directory {output_directory} is not empty"
                )

    pull_layers_in_threads(drc, layers, output_directory)

    if tar_file:
        cwd = os.getcwd()
        os.chdir(output_directory)
        with tarfile.open(tar_file, "w:gz") as tar:
            tar.add(".", arcname="", recursive=True)
        os.chdir(cwd)

    if squashfs_file:
        squafshfs_file = Path(squashfs_file)
        if squafshfs_file.exists():
            squafshfs_file.unlink()
        print("Creating squashfs file...", end="", flush=True)
        exit_code, output = getstatusoutput(
            f"mksquashfs {output_directory} {squafshfs_file}"
        )
        if exit_code != 0:
            raise typer.Exit(f"Failed to create squashfs file: {output}")
        print("Done")

    if not is_tmp_output_directory:
        print(f"Contents of {source_reference} extracted to {output_directory}")


def parse_image_url(image_name: str) -> tuple:
    registry = DEFAULT_REGISTRY
    tag = "latest"
    if "/" in image_name:
        first_part, other_parts = image_name.split("/", 1)
        if "." in first_part:
            image_name = other_parts
            registry = f"{first_part}"
    else:
        image_name = f"library/{image_name}"
    if ":" in image_name:
        image_name, tag = image_name.split(":")
    return registry, image_name, tag
