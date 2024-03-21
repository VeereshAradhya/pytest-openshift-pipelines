from kubernetes import config
from kubernetes import dynamic
from kubernetes.client import api_client
import urllib3

# Ignore warnings
urllib3.disable_warnings()


class ClientBase:
    """
    Base class for all the clients
    """

    def __init__(self):
        """
        Uses existing kubeconfig
        TODO: Update the constructor to use given kubeconfig
        """
        config.load_config()


class DynamicClientBase(ClientBase):
    """
    Base class for all the dynamic clients
    """
    API_VERSION = ""
    KIND = ""

    def __init__(self):
        super().__init__()
        self.client = dynamic.DynamicClient(api_client.ApiClient())
        self.api = self.client.resources.get(api_version=self.API_VERSION, kind=self.KIND)

    def _list(self, namespace: str = "", name: str = ""):
        return self.api.get(namespace=namespace, name=name)

    def _create(self, body: dict, namespace: str):
        return self.api.create(body=body, namespace=namespace)

    def _delete(self, name: str, namespace: str):
        return self.api.delete(name=name, namespace=namespace, body={})
