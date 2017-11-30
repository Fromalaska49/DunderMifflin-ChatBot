from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView


# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import render
#
# from ChatBot.views.misc.Constants import ERROR
from ChatBot import models


class EditUser(ListView):
    #gets instance of user and allows for only authorized
    #edits. User must be logged in
    model = models.User
    success_url = reverse_lazy('login_handler')
    success_message = "Your changes have been saved."
    template_name = 'edit/edit_user.html'


    def get_object(self):
        messages.success(self.request, self.success_message)
        return get_object_or_404(User, pk=self.request.user.id)
