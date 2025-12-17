from mlops.features.build_features import build_features


def test_build_features_empty_dataframe():
    import pandas as pd

    df = pd.DataFrame()
    out = build_features(df)
    assert out.equals(df)
