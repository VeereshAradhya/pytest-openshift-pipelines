from osp.common.client_base import DynamicClientBase
from osp.util.util import poller


class Subscription(DynamicClientBase):
    """
    Client to access subscription custom resource
    """
    API_VERSION = "operators.coreos.com/v1alpha1"
    KIND = "Subscription"

    def list_subscriptions(self, namespace: str):
        """
        lists the subscriptions of a given namespace
        :param namespace: object name and auth scope, such as for teams and projects (required)
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list(namespace=namespace)

    def list_subscriptions_for_all_namespace(self):
        """
        lists subscriptions from all namespaces
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list()

    def get_subscription(self, namespace: str, name: str):
        """
        get a particular subscription
        :param namespace: object name and auth scope, such as for teams and projects (required)
        :param name: name of the subscription
        :return: kubernetes.dynamic.resource.ResourceInstance
        """
        return self._list(namespace=namespace, name=name)

    def create_subscription(self, name: str, namespace: str, catalog_source: str,
                            catalog_source_namespace: str,
                            install_plan: str, channel: str):
        """
        Create subscription
        :param name: name of the subscription
        :param namespace: namespace on which the operator needs to be created
        :param catalog_source: name of the catalog source
        :param catalog_source_namespace: namespace where the catalog source resides
        :param install_plan: install plan type (Manual|Automatic)
        :param channel: name of the channel
        """
        subscription_manifest = {
            "apiVersion": "operators.coreos.com/v1alpha1",
            "kind": "Subscription",
            "metadata": {"name": name},
            "spec": {
                "channel": channel,
                "installPlanApproval": install_plan,
                "name": name,
                "source": catalog_source,
                "sourceNamespace": catalog_source_namespace
            }
        }
        self._create(body=subscription_manifest, namespace=namespace)

    def wait_for_subscription_status(self, name: str, namespace: str,
                                     status: str, interval: int, timeout: int) -> str:
        """
        Wait till the subscription is in expected status
        :param name: name of the subscription
        :param namespace: namespace in which the subscription is present
        :param status: expected status of the subscription
        :param interval: interval in which we poll
        :param timeout: polling timeout
        :return: final status of the subscription after timeout
        """
        polling = poller(interval=interval, timeout=timeout)
        sub = self.get_subscription(name=name, namespace=namespace)
        for _ in polling:
            print(f"waiting for the status of subscription {name} in namespace {namespace} to be {status}")
            if sub.status.conditions[0]["status"] == status:
                break
            sub = self.get_subscription(name=name, namespace=namespace)
        return sub.status.conditions[0]["status"]

    def delete_subscription(self, name: str, namespace: str):
        """
        Delete a subscription
        :param name: name of the subscription
        :param namespace: namespace in which the subscription is present
        :return:
        """
        return self._delete(name=name, namespace=namespace)
