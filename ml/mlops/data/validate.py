from .schemas import InputRow


def validate_row(d: dict) -> InputRow:
    return InputRow(**d)
