import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.urls import reverse
from ChatBot.views.misc.Constants import *


from ChatBot.forms import UserProfileForm


@login_required(login_url='login')
def update_user(request, template_name="update/update_profile.html"):
    response_data = {}
    response_data[ERROR] = True
    try:
        current_user = request.user
        user = User.objects.get(email=current_user)
    except Exception:
        return render(request, 'admin/login.html')
    else:
        if request.method == "POST":
            form = UserProfileForm(request.POST, instance=user)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                response_data[ERROR] = False
                response_data[MSG] = UPDATE_SUCCESS
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            form = UserProfileForm(instance=request.user)

        return render(request, template_name, {
            'form': form})
