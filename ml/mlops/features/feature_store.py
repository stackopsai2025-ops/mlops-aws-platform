class FeatureStoreClient:
    def read(self, key):
        raise NotImplementedError

    def write(self, key, df):
        raise NotImplementedError
