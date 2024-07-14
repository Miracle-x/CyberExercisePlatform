import docker
from config.settings import config

class DockerService:
    def __init__(self):
        self.client = docker.from_env()

    def create_container(self, image, name, command=None):
        container = self.client.containers.run(
            image,
            command=command,
            name=name,
            detach=True
        )
        return container

    def stop_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()
        container.remove()
