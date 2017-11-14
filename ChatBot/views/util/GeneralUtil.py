from ChatBot.views.misc.Constants import INPUT


def getUserInput(request):
    user_input = request.POST.get(INPUT)

    if input is None:
        raise Exception('INPUT REQUEST PARAMETER NOT FOUND')

    else:
        return user_input
