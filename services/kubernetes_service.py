from kubernetes import client, config
from config.settings import config as app_config

class KubernetesService:
    def __init__(self):
        config.load_kube_config(app_config['kubernetes']['config_file'])
        self.api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()

    def create_namespace(self, name):
        namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
        self.api.create_namespace(namespace)

    def delete_namespace(self, name):
        self.api.delete_namespace(name)

    def create_pod(self, namespace, name, image):
        pod = client.V1Pod(
            metadata=client.V1ObjectMeta(name=name),
            spec=client.V1PodSpec(
                containers=[client.V1Container(
                    name=name,
                    image=image
                )]
            )
        )
        self.api.create_namespaced_pod(namespace=namespace, body=pod)

    def delete_pod(self, namespace, name):
        self.api.delete_namespaced_pod(name=name, namespace=namespace)
