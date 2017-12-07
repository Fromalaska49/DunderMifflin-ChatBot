"""ChatBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.views import password_change, password_change_done
from ChatBot.forms import ValidatingPasswordChangeForm
from .views.account_management.ChangePassword import ChangePassword
from ChatBot.views.update_user.UpdateUserProfile import update_user
from .views.delete_user.DeleteUser import DeleteUser
from .views.registration.UserRegistration import UserRegistration
from .views.chatbot_service.ChatBotHandler import ChatBotHandler
from .views.chatbot_service.ChatBotEmbedHandler import ChatBotEmbedHandler
from .views.account_management.UnlockAccount import UnlockAccount
from .views.account_management.VerifyAccount import VerifyAccount
from .views.account_management.RequestChange import RequestChange
from .views.account_management.ResetPassword import ResetPassword
from .views.intent_management.GetIntent import GetIntent
from .views.intent_management.GetIntents import GetIntents
from .views.intent_management.RemoveIntent import RemoveIntent
from .views.intent_management.AddIntent import AddIntent
from .views.login.Login import Login
from django.contrib import auth
from .views.forgot.Forgot import Forgot
from django.contrib import admin

urlpatterns = [
    url(r'^admin/login/?', Login.as_view(), name="admin_login_handler"),  # will override admin login page
    url(r'^admin/?', admin.site.urls),
    url(r'^$', Login.as_view(), name="login"),
    url(r'^register', UserRegistration.as_view(), name="registration"),
    url(r'^registration', UserRegistration.as_view(), name="registration"),
    url(r'^requestchange', RequestChange.as_view(), name="update_info_handler"),
    url(r'^reset/(?P<token>\w{12})', ResetPassword.as_view(), name="account_verification_handler"),
    url(r'^reset', ResetPassword.as_view(), name="account_verification_handler"),
    url(r'^verify/(?P<token>\w{12})', VerifyAccount.as_view(), name="account_verification_handler"),
    url(r'^unlock/(?P<token>\w{12})', UnlockAccount.as_view(), name="account_unlocking_handler"),
    url(r'^login', Login.as_view(), name="login_handler"),
    url(r'^chatbot', ChatBotHandler.as_view(), name="chatbot_handler"),
    url(r'^embed', ChatBotEmbedHandler.as_view(), name="embed_handler"),
    url(r'^delete', DeleteUser.as_view(), name="delete_user_handler"),
    url(r'^forgot', Forgot.as_view(), name="forgot_handler"),
    url(r'^update', update_user, name="update_profile_handler"),
    url(r'^logout', auth.views.logout, name='logout_handler', kwargs={'next_page': 'login_handler'}),
    url(r'^change', ChangePassword.as_view(), name="change_password_handler"),
    url(r'^change_password', password_change,
        {'password_change_form': ValidatingPasswordChangeForm}),
    url(r'^password_changed', password_change_done, {'template_name': 'change_password/change_password.html'},
        name='password_change_done'),
    url(r'^delete_success', DeleteUser.as_view(), name="delete_success_handler"),
    url(r'^get_intents', GetIntents.as_view(), name="get_intents"),
    url(r'^get_intent', GetIntent.as_view(), name="get_intent"),
    url(r'^get_intents', GetIntents.as_view(), name="get_intents"),
    url(r'^remove_intent', RemoveIntent.as_view(), name="remove_intent"),
    url(r'^add_intent', AddIntent.as_view(), name="add_intent")
]
