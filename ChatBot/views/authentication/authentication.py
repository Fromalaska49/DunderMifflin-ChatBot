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


def authenticate(request):

    auth_return = {}
    state = request.session.get(LOGIN_MACHINE_STATE)

    # retrieve username, move to USERNAME_STATE
    if state == NULL_STATE:
        print 'GETTING EMAIL FOR LOGIN'
        email = request.POST.get(INPUT)
        request.session[EMAIL] = email
        request.session[LOGIN_MACHINE_STATE] = USERNAME_STATE
        auth_return[RET_CODE] = PASSWORD_REQUIRED
        print 'RETRIEVED EMAIL. MOVED TO USERNAME_STATE'
        return auth_return

    # retrieve password and authenticate. Move to NULL_STATE reguardless of outcome (reset machine)
    elif state == USERNAME_STATE:
        password = request.POST.get(INPUT)
        email = request.session.get(EMAIL)

        # if not user_exists(email):
        # auth_return[RET_CODE] = INVALID_CREDENTIALS
        # return auth_return

        if login_attempts_exceeded(request.session):
            # lock account with added variable
            auth_return[RET_CODE] = ACCOUNT_LOCKED
            return auth_return

        user = django_auth(request, username=email, password=password)

        if user is None:

            request.session[LOGIN_MACHINE_STATE] = NULL_STATE
            increment_login_attempts(request.session)
            auth_return[RET_CODE] = INVALID_CREDENTIALS
            return auth_return

        else:

            reset_login_attempts(request.session)

            if user.is_active:
                auth_return[RET_CODE] = AUTH_SUCCESS
                auth_return[USER] = user
                return auth_return

            else:
                auth_return[RET_CODE] = ACCOUNT_INACTIVE
                return auth_return

    else:
        print 'UNRECOGNIZED STATE: ' + state
        request.session[LOGIN_MACHINE_STATE] = NULL_STATE
        auth_return[RET_CODE] = ERROR
        return auth_return

