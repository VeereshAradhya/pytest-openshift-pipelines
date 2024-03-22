from osp.common.client_base import DynamicClientBase


class Namespace(DynamicClientBase):
    API_VERSION = "v1"
    KIND = "Namespace"

    def create_namespace(self, name: str) -> str:
        """
        Creates namespace with a given name
        :param name:
        :return: created namespace object
        """
        namespace_manifest = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": name, "resourceversion": "v1"},
        }
        return self._create(body=namespace_manifest, namespace="")

    def delete_namespace(self, name: str):
        return self._delete(name=name, namespace="")
