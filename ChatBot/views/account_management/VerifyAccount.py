from django.views.generic import ListView
from ChatBot.models import User
from django.http import HttpResponse, HttpResponseRedirect
from ChatBot.views.util.EmailUtil import send_admin_verified_email
from ChatBot.views.util.AuthenticationUtil import reset_login_attempts
from ChatBot.views.misc.Constants import HTTP_HOST
from django.http import Http404


class VerifyAccount(ListView):

    def get(self, request, token):

        if token is None:
            raise Http404()

        if User.objects.filter(acct_verification_token=token).exists():
            user = User.objects.get(acct_verification_token=token)
            user.acct_active = True
            user.acct_verification_token = ''
            reset_login_attempts(request.session, user.email)
            user.save()

            if user.is_staff:
                send_admin_verified_email(user.email, request.META[HTTP_HOST])

            return HttpResponseRedirect("/login")

        else:
            raise Http404()
