from drclient.image import parse_image_url


def test_registry_urls():
    registry, image, tag = parse_image_url("ubuntu")
    assert (registry, image, tag) == (
        "registry-1.docker.io",
        "library/ubuntu",
        "latest",
    )

    registry, image, tag = parse_image_url("python:3.10")
    assert (registry, image, tag) == ("registry-1.docker.io", "library/python", "3.10")

    registry, image, tag = parse_image_url(
        "ghcr.io/deselikem/hello-docker-gcr-demo:latest"
    )
    assert (registry, image, tag) == (
        "ghcr.io",
        "deselikem/hello-docker-gcr-demo",
        "latest",
    )
