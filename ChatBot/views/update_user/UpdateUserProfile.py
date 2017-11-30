from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from ChatBot.forms import UserProfileForm


@login_required()
def update_user(request, template_name="update/update_profile.html"):
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
                #messages.success(request, "Account profile has been updated")
                url = urlresolvers.reverse('update_profile_handler')
                return HttpResponseRedirect(url)
        else:
            form = UserProfileForm(instance=request.user)

        return render(request, template_name, {
            'form': form})
