from osp.common.main import OSPMain


class OSPTestCase:
    OSP = OSPMain

    @classmethod
    def setup_class(cls):
        cls.OSP = OSPMain()
