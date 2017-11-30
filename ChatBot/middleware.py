import datetime
from django.contrib.auth.views import logout, login
from django.utils.deprecation import MiddlewareMixin

from ChatBot import settings


class AutoLogout(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated():
            current_datetime = datetime.datetime.now()
            if 'last_login' in request.session:
                last = (current_datetime - request.session['last_login']).seconds
                if last > settings.SESSION_IDLE_TIMEOUT:
                    logout(request, login.html)
            else:
                request.session['last_login'] = current_datetime
        return None
