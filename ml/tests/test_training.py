from mlops.training.train import train_model


def test_train_placeholder():
    assert train_model([], [])["status"] == "trained"
