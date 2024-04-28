from osp.common.client_base import DynamicClientBase
from osp.util.util import poller


class PipelineRun(DynamicClientBase):
    """
    Client to access pipelinerun custom resource
    """
    API_VERSION = "tekton.dev/v1"
    KIND = "PipelineRun"

    def list_pipelineruns(self, namespace: str):
        """
        lists the pipelinerun of a given namespace
        :param namespace: object name and auth scope, such as for teams and projects (required)
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list(namespace=namespace)

    def list_pipelineruns_for_all_namespace(self):
        """
        lists pipelineruns from all namespaces
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

    def wait_for_pipelinerun_complete(self, name: str, namespace: str, interval: int, timeout: int):
        """
        Waits till the pipelinerun reaches expected status
        :param name: name of the pipelinerun
        :param namespace: namespace in which the pipelinerun is present
        :param interval: interval for polling
        :param timeout: polling timeout
        :return: found status after timeout
        """
        pipelinerun_resource = self.get_pipelinerun(name=name, namespace=namespace)
        polling = poller(interval=interval, timeout=timeout)
        for _ in polling:
            if pipelinerun_resource.status.conditions[0]["reason"] != "Running":
                break
            pipelinerun_resource = self.get_pipelinerun(name=name, namespace=namespace)
        return pipelinerun_resource.status.conditions[0]["status"]
