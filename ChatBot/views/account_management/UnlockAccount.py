from django.views.generic import ListView
from ChatBot.models import User
from django.http import HttpResponse
from ChatBot.views.util.AuthenticationUtil import reset_login_attempts


class UnlockAccount(ListView):

    def get(self, request, token):
        print token

        if token is None:
            # return 404
            pass

        if User.objects.filter(acct_locked_token=token).exists():
            user = User.objects.get(acct_locked_token=token)
            user.is_locked = False
            user.acct_locked_token = ''
            reset_login_attempts(request.session, user.email)
            user.save()
            return HttpResponse("Your account has been successfully unlocked!")


        else:
            # return 404
            pass
