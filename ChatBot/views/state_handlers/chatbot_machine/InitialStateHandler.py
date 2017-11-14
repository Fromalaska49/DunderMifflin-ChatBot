from ChatBot.views.misc.Constants import *
from ChatBot.views.util.GeneralUtil import getUserInput


def handle_initial_state(request):
    user_input = getUserInput(request)
    initial_state_return = {}
    initial_state_return[ERROR] = False

    # Perform NLP on input here

    # If NLP determines login request, transition into login state and begin handling
    # (hard comparison against 'login' for now)
    if user_input == "login":
        request.session[CHATBOT_MACHINE_STATE] = LOGIN_STATE
        initial_state_return[MSG] = ENTER_EMAIL

    # else if NLP determines account recovery request, change to account recovery state and begin handling
    # (hard comparison against account recovery for now)
    elif user_input == 'account recovery':
        pass

    # else, unrecognized input, send welcome message again or instruct them to request login or account recovery
    else:
        initial_state_return[RET_CODE] = AMBIGUOUS
        initial_state_return[MSG] = INITIAL_HELP

    return initial_state_return
