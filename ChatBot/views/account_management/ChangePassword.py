import json
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from ChatBot.forms import ValidatingPasswordChangeForm
from ChatBot.views.misc.Constants import *


class ChangePassword(LoginRequiredMixin, ListView, PasswordChangeForm):
    def post(self, request):
        response_data = {}
        response_data[ERROR] = True
        # if request.method == 'POST':
        form = ValidatingPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            response_data[ERROR] = False
            response_data[MSG] = PASS_CHANGE_SUCCESS
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            messages.error(request, ('Please correct the error below.'))
            # else:
            # form = PasswordChangeForm(request.user)
        return render(request, "change_password/change_password.html", {
            'form': form
        })

    def get(self, request):
        form = ValidatingPasswordChangeForm(request.user)
        return render(request, "change_password/change_password.html", {
            'form': form
        })

    # def clean_password1(self):
    #     password_val = validate_password(self.cleaned_data['password1'])
    #     if password_val[ERROR] is True:
    #         raise ValidationError(password_val(ERROR))
    #         #response_data = password_val
    #     else:
    #         return validate_password(self.cleaned_data['password1'])

