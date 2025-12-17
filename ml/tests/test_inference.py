from mlops.inference.predictor import Predictor


def test_predictor_returns_list():
    p = Predictor()
    out = p.predict([1, 2, 3])
    assert isinstance(out, list) and len(out) == 3
