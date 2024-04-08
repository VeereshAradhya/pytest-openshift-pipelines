import os
from osp.common.osp_base_test import OSPTestCase
from osp.util.util import oc_create


class TestPipelines(OSPTestCase):
    @classmethod
    def setup_class(cls):
        super().setup_class()

    def setup_method(self):
        self.namespace = self.create_namespace_with_random_name()

    def teardown_method(self):
        self.delete_namespace(self.namespace)

    def test_simple_pipeline_creation(self):
        currentDir = os.path.dirname(__file__)
        stdout, stderr, returncode = oc_create(f"{currentDir}/testdata/simple_pipeline.yaml", self.namespace)
        bp = self.OSP.api.pipelines.get_pipeline(name="buildah-pipeline", namespace=self.namespace)
        assert returncode == 0, stderr
        assert bp["metadata"]["name"] == "buildah-pipeline"
