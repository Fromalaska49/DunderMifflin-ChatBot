from django.contrib.auth import authenticate as django_auth
from django.contrib.auth.models import User

#THESE METHODS HANDLE AUTHENTICATION ONLY
#LOGIN FUNCTIONALITY HANDLED SEPARATELY, AS WE WILL
#NEED TO AUTHENTICATE A LOGGED IN USER WHEN UPDATING INFORMATION

NULL_STATE = None
USERNAME_STATE = 'USERNAME_STATE'
LOGIN_STATE_MACHINE = 'LOGIN_STATE_MACHINE'

#request param constant
INPUT = 'input'

#session attribute label constant
EMAIL = 'email'
LOGIN_ATTEMPTS = 'login_attempts'

#return codes
RET_01 = 'PASSWORD_REQUIRED'
RET_02 = 'INVALID_CREDENTIALS'
RET_03 = 'ACCOUNT_LOCKED'
RET_04 = 'ACCOUNT_INACTIVE'
RET_05 = 'AUTH_SUCCESS'
RET_06 = 'ERROR'

LOGIN_ATTEMPT_LIMIT = 5


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

    state = request.session.get(LOGIN_STATE_MACHINE)

    #retrieve username, move to USERNAME_STATE
    if state == NULL_STATE:
        email = request.POST.get(INPUT)
        request.session[EMAIL] = email
        request.session[LOGIN_STATE_MACHINE] = USERNAME_STATE
        return RET_01

    #retrieve password and authenticate. Move to NULL_STATE reguardless of outcome (reset machine)
    elif state == USERNAME_STATE:
        password = request.POST.get(INPUT)
        email = request.session.get(EMAIL)

        if not user_exists(email):
            return RET_02

        if login_attempts_exceeded(request.session):
            #lock account with added variable
            return RET_03

        user = django_auth(request, username=email, password=password)

        if user is None:

            request.session[LOGIN_STATE_MACHINE] = NULL_STATE
            increment_login_attempts(request.session)

        else:

            reset_login_attempts(request.session)

            if user.is_active:
                return RET_05
            else:
                return RET_04

    else:
        print 'UNRECOGNIZED STATE: ' + state
        request.session[LOGIN_STATE_MACHINE] = NULL_STATE
        return RET_06

