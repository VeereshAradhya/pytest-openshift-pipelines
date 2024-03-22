import string
import random
from osp.common.main import OSPMain


class OSPTestCase:
    OSP = OSPMain

    @classmethod
    def setup_class(cls):
        cls.OSP = OSPMain()

    def create_namespace_with_random_name(self, name_prefix: str = "osp-tests"):
        res = ''.join(random.choices(string.ascii_lowercase +
                                     string.digits, k=6))
        namespace_name = f"{name_prefix}-res"
        self.OSP.utils.namespace.create_namespace(name=namespace_name)
        return namespace_name
