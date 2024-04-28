import logging
import string
import random
from osp.common.main import OSPMain


class OSPTestCase:
    OSP = OSPMain
    logger = logging.getLogger("test")

    @classmethod
    def setup_class(cls):
        cls.OSP = OSPMain()
        cls.logger.setLevel("INFO")

    def create_namespace_with_random_name(self, name_prefix: str = "osp-tests"):
        res = ''.join(random.choices(string.ascii_lowercase +
                                     string.digits, k=6))
        namespace_name = f"{name_prefix}-{res}"
        self.logger.info("Creating a namespace with name %s", namespace_name)
        self.OSP.utils.namespace.create_namespace(name=namespace_name)
        return namespace_name

    def delete_namespace(self, name):
        self.logger.info("Deleting a namespace with name %s", name)
        self.OSP.utils.namespace.delete_namespace(name)