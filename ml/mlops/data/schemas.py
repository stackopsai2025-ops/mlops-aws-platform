from pydantic import BaseModel


class InputRow(BaseModel):
    id: int
    feature_a: float
    feature_b: float
