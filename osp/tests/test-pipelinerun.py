import os
from osp.common.osp_base_test import OSPTestCase
from osp.util.util import oc_create


class TestPipelineruns(OSPTestCase):
    @classmethod
    def setup_class(cls):
        super().setup_class()

    def setup_method(self):
        self.namespace = self.create_namespace_with_random_name()

    def teardown_method(self):
        self.delete_namespace(self.namespace)

    def test_simple_pipelinerun_success(self):
        currentDir = os.path.dirname(__file__)
        stdout, stderr, returncode = oc_create(f"{currentDir}/testdata/simple_pipelinerun.yaml", self.namespace)
        status = self.OSP.api.pipelinerun.wait_for_pipelinerun_complete(name="simple-pipelinerun", namespace=self.namespace, interval=10, timeout=120)
        assert status == "True"
    
    def test_simple_pipelinerun_failure(self):
        currentDir = os.path.dirname(__file__)
        stdout, stderr, returncode = oc_create(f"{currentDir}/testdata/simple_pipelinerun_failure.yaml", self.namespace)
        status = self.OSP.api.pipelinerun.wait_for_pipelinerun_complete(name="simple-pipelinerun-failure", namespace=self.namespace, interval=10, timeout=120)
        assert status == "False"
    