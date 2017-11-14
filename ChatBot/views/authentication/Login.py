from Authentication import *
from django.contrib.auth import login as django_login
from ChatBot.views.misc.GlobalDictKeys import *
from ChatBot.views.misc.ChatBotResponses import *
from ChatBot.views.misc.ChatBotStates import *
from ChatBot.views.misc.GlobalDictKeys import CHATBOT_MACHINE_STATE


def login(request):

    login_return = {}
    auth_return = authenticate(request)

    print 'AUTHENTICATE RET CODE: ' + auth_return[RET_CODE]

    if auth_return[RET_CODE] == PASSWORD_REQUIRED:
        login_return[ERROR] = False
        login_return[MSG] = ENTER_PASSWORD

    if auth_return[RET_CODE] == INVALID_CREDENTIALS:
        pass

    if auth_return[RET_CODE] == ACCOUNT_LOCKED:
        pass

    if auth_return[RET_CODE] == ACCOUNT_INACTIVE:
        pass

    if auth_return[RET_CODE] == AUTH_SUCCESS:
        django_login(request, auth_return[USER])
        login_return[ERROR] = False
        login_return[MSG] = LOGIN_SUCCESS
        request.session[CHATBOT_MACHINE_STATE] = AUTHENTICATED_INPUT_STATE
        print 'AUTHENTICATION SUCCESSFUL. CHATBOT MACHINE NOW AT STATE: ' + AUTHENTICATED_INPUT_STATE

    if auth_return[RET_CODE] == ERROR:
        pass

    return login_return
