from ChatBot.views.state_handlers.login_sub_machine.LoginSubStateMachineHandler import perform_login
from django.contrib.auth import login as django_login
from ChatBot.views.misc.Constants import *


def handle_login_state(request):

    login_return = {}
    auth_return = perform_login(request)
    login_return[ERROR] = False

    print 'AUTHENTICATE RET CODE: ' + auth_return[RET_CODE]

    if auth_return[RET_CODE] == PASSWORD_REQUIRED:
        login_return[MSG] = ENTER_PASSWORD

    if auth_return[RET_CODE] == INVALID_CREDENTIALS:
        request.session[CHATBOT_MACHINE_STATE] = INITIAL_STATE
        login_return[MSG] = COMBINATION_INVALID

    if auth_return[RET_CODE] == ACCOUNT_LOCKED:
        request.session[CHATBOT_MACHINE_STATE] = INITIAL_STATE
        login_return[MSG] = ATTEMPTS_EXCEEDED

    if auth_return[RET_CODE] == ACCOUNT_INACTIVE:
        request.session[CHATBOT_MACHINE_STATE] = INITIAL_STATE
        login_return[MSG] = ACCOUNT_NOT_VERIFIED

    if auth_return[RET_CODE] == AUTH_SUCCESS:
        request.session[CHATBOT_MACHINE_STATE] = INQUIRE_STATE
        login_return[MSG] = LOGIN_SUCCESS
        print 'AUTHENTICATION SUCCESSFUL. CHATBOT MACHINE NOW AT STATE: ' + INQUIRE_STATE

    if auth_return[RET_CODE] == ERROR:
        request.session[CHATBOT_MACHINE_STATE] = INITIAL_STATE
        login_return[ERROR] = True
        login_return[MSG] = 'Stuff went wrong'

    return login_return
