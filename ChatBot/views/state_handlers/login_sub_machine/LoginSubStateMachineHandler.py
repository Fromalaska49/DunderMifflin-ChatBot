from django.contrib.auth import login as django_login

from ChatBot.views.misc.Constants import *
from ChatBot.views.util.AuthenticationUtil import *
from ChatBot.views.util.GeneralUtil import getUserInput


def perform_login(request):

    return_structure = {}
    state = request.session.get(LOGIN_MACHINE_STATE)

    # retrieve username, move to USERNAME_STATE
    if state == NULL_STATE:
        print 'GETTING EMAIL FOR LOGIN'
        email = getUserInput(request)
        request.session[EMAIL] = email
        request.session[LOGIN_MACHINE_STATE] = EMAIL_STATE
        return_structure[RET_CODE] = PASSWORD_REQUIRED
        print 'RETRIEVED EMAIL. MOVED TO USERNAME_STATE'
        return return_structure

    # retrieve password and authenticate. Move to NULL_STATE reguardless of outcome (reset machine)
    elif state == EMAIL_STATE:
        password = getUserInput(request)
        email = request.session.get(EMAIL)

        if login_attempts_exceeded(request.session):
            # lock account with added variable
            return_structure[RET_CODE] = ACCOUNT_LOCKED
            return return_structure

        user = django_auth(request, username=email, password=password)

        if user is None:
            request.session[LOGIN_MACHINE_STATE] = NULL_STATE
            increment_login_attempts(request.session)
            return_structure[RET_CODE] = INVALID_CREDENTIALS
            return return_structure

        else:
            reset_login_attempts(request.session)

            if user.is_active:
                django_login(request, user)
                return_structure[RET_CODE] = AUTH_SUCCESS
                return return_structure

            else:
                return_structure[RET_CODE] = ACCOUNT_INACTIVE
                return return_structure

    else:
        print 'UNRECOGNIZED STATE: ' + state
        request.session[LOGIN_MACHINE_STATE] = NULL_STATE
        return_structure[RET_CODE] = ERROR
        return return_structure
