
class ValidationError(Exception):
    pass


def validate(kwarg, validator, validator_string):
    try:
        if isinstance(validator, dict):
            validator = list(validator.keys())
        assert kwarg in validator
    except AssertionError:
        raise ValidationError(
            f'{kwarg} is an invalid {validator_string} keyword. Use the following. {validator}')
