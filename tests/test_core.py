from prefect import flow
from prefect.orion.schemas.states import StateType

from prefect_docker import list_containers, list_images, pull_image, run_container


@flow
def myflow():
    list_containers(all=True)
    list_images()
    pull_image("hello-world")
    run_container(image="hello-world")


def test_core():
    states = myflow()
    assert [state.type == StateType.COMPLETED for state in states]
