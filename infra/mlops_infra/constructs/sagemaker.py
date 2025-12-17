from constructs import Construct


class SageMakerConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id)
        # TODO: SageMaker helpers
