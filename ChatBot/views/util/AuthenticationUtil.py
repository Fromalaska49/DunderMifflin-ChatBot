from django.contrib.auth import authenticate as django_auth
from django.contrib.auth.models import User
from ChatBot.views.misc.Constants import *

# THESE METHODS HANDLE AUTHENTICATION ONLY
# LOGIN FUNCTIONALITY HANDLED SEPARATELY, AS WE WILL
# NEED TO AUTHENTICATE A LOGGED IN USER WHEN UPDATING INFORMATION


def user_exists(email):

    if email is None:
        return False

    if User.objects.filter(username=email).exists():
        return True
    else:
        return False


def reset_login_attempts(session):

    email = session.get(EMAIL)

    if email is None:
        raise Exception('NO EMAIL FOUND IN SESSION WHILE RESETTING LOGIN ATTEMPTS')

    if session.get(LOGIN_ATTEMPTS) is None:
        session[LOGIN_ATTEMPTS] = {}

    attempts = session[LOGIN_ATTEMPTS].get(email)

    if attempts is not None:
        session[LOGIN_ATTEMPTS][email] = None


def increment_login_attempts(session):

    email = session.get(EMAIL)

    if email is None:
        raise Exception('NO EMAIL FOUND IN SESSION WHILE INCREMENTING LOGIN ATTEMPTS')

    if session.get(LOGIN_ATTEMPTS) is None:
        session[LOGIN_ATTEMPTS] = {}

    attempts = session[LOGIN_ATTEMPTS].get(email)

    if attempts is None:
        session[LOGIN_ATTEMPTS][email] = 1

    else:
        session[LOGIN_ATTEMPTS][email] = attempts + 1

    session.modified = True


def login_attempts_exceeded(session):

    email = session.get(EMAIL)

    if email is None:
        raise Exception('NO EMAIL FOUND IN SESSION WHILE VERIFYING LOGIN ATTEMPTS')

    if session.get(LOGIN_ATTEMPTS) is None:
        session[LOGIN_ATTEMPTS] = {}

    attempts = session[LOGIN_ATTEMPTS].get(email)

    if attempts is None:
        return False

    if attempts > LOGIN_ATTEMPT_LIMIT:
        return True
