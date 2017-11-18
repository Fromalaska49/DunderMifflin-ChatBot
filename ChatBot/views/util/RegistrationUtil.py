from ChatBot.views.misc.Constants import *
from django.contrib.auth.models import User
import re


def validate_email(email):
    matcher = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')

    if matcher.match(email) is None:
        return False

    return True


def validate_password(password):

    return_structure = {}
    return_structure[ERROR] = True

    if re.search(r'(?=(?:.*[A-Z]){2})', password) is None:
        return_structure[MSG] = PASS_UPPERCASE_ERROR

    elif re.search(r'(?=(?:.*[!@#$%&*-+]){2})', password) is None:
        return_structure[MSG] = PASS_SYMBOL_ERROR

    elif re.search(r'(?=(?:.*[0-9]){2})', password) is None:
        return_structure[MSG] = PASS_NUMBER_ERROR

    elif not len(password) >= 8:
        return_structure[MSG] = PASS_LENGTH_ERROR

    else:
        return_structure[ERROR] = False

    return return_structure


def validate_credentials(email, password, password_conf):
    response_data = {}
    password_val = validate_password(password)

    if not validate_email(email):
        response_data[ERROR] = True
        response_data[MSG] = EMAIL_INVALID_ERROR

    elif User.objects.filter(email=email).exists():
        response_data[ERROR] = True
        response_data[MSG] = EMAIL_TAKEN_ERROR

    elif password != password_conf:
        response_data[ERROR] = True
        response_data[MSG] = PASS_MATCH_ERROR

    elif password_val[ERROR] is True:
        response_data = password_val

    else:
        response_data[ERROR] = False

    return response_data
