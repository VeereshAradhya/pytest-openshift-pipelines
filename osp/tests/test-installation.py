from osp.common.osp_base_test import OSPTestCase


class TestInstallation(OSPTestCase):
    @classmethod
    def setup_class(cls):
        super().setup_class()

    def teardown_method(self):
        self.OSP.utils.subscriptions.delete_subscription(namespace="openshift-operators",
                                                         name="openshift-pipelines-operator-rh")

    def test_installation_invalid(self):
        self.OSP.utils.subscriptions.create_subscription(name="openshift-pipelines-operator-rh",
                                                         namespace="openshift-operators",
                                                         catalog_source="redhat-operators", install_plan="Automatic",
                                                         channel="pipelines-1.19",
                                                         catalog_source_namespace="openshift-marketplace")
        installation_status = self.OSP.utils.subscriptions.wait_for_subscription_status(
            name="openshift-pipelines-operator-rh", namespace="openshift-operators", status="True", interval=5,
            timeout=120)
        assert installation_status == "False"

    def test_installation_valid(self):
        """
        TODO:
        1. Verify the deployments that gets created when the operator is installed
        """
        self.OSP.utils.subscriptions.create_subscription(name="openshift-pipelines-operator-rh",
                                                         namespace="openshift-operators",
                                                         catalog_source="redhat-operators", install_plan="Automatic",
                                                         channel="pipelines-1.14",
                                                         catalog_source_namespace="openshift-marketplace")
        installation_status = self.OSP.utils.subscriptions.wait_for_subscription_status(
            name="openshift-pipelines-operator-rh", namespace="openshift-operators", status="True", interval=5,
            timeout=120)
        assert installation_status == "True"
