from osp.api.pipeline import Pipeline
from osp.api.pipelinerun import PipelineRun
from osp.util.subscription import Subscription
from osp.util.namespace import Namespace
from kubernetes.dynamic.exceptions import ResourceNotFoundError


class OSPBase:
    def __init__(self):
        # Initialising all the class variables
        for attr in dir(self):
            if not attr.startswith("_"):
                member = getattr(self, attr)
                try:
                    setattr(self, attr, member())
                except ResourceNotFoundError:
                    # Skipping creation of instance for the resources which are not present yet.
                    pass


class API(OSPBase):
    pipelines = Pipeline
    pipelinerun = PipelineRun


class Utils(OSPBase):
    subscriptions = Subscription
    namespace = Namespace


class OSPMain(OSPBase):
    api = API
    utils = Utils


if __name__ == "__main__":
    osp = OSPMain()
