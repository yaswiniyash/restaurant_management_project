from django.core.validators import validate_email
from django.core.exceptions import validationError

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except validationError:
        return False
