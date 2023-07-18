from re import fullmatch

from django.core.exceptions import ValidationError


def username_validator(value):
    if value == 'me':
        raise ValidationError(
            'Имя пользователя не может быть <me>.',
            params={'value': value},
        )
    if fullmatch(r'^[\w.@+-]+$', value) is None:
        raise ValidationError(
            'В имени пользователя допускаются только '
            'буквы, цифры и следующие знаки: @.+-',
            params={'value': value},
        )
    return value
