from osp.common.client_base import DynamicClientBase


class PipelineRun(DynamicClientBase):
    """
    Client to access pipeline custom resource
    """
    API_VERSION = "tekton.dev/v1"
    KIND = "PipelineRun"

    def list_pipelinerun(self, namespace: str):
        """
        lists the pipelines of a given namespace
        :param namespace: object name and auth scope, such as for teams and projects (required)
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list(namespace=namespace)

    def list_pipelinerun_for_all_namespace(self):
        """
        lists pipelines from all namespaces
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list()

    def get_pipelinerun(self, namespace: str, name: str):
        """
        :param namespace: object name and auth scope, such as for teams and projects (required)
        :param name: name of the pipeline
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list(namespace=namespace, name=name)