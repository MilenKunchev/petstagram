from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            # invalid case
            raise ValidationError('Value must contain only letters')
    # valid case
