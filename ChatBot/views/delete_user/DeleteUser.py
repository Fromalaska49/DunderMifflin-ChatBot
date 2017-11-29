# from django.contrib.auth.decorators import login_required
# from django.forms import forms
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView


# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import render
#
# from ChatBot.views.misc.Constants import ERROR
from ChatBot import models


class DeleteUser(DeleteView):
    model = models.User
    success_url = reverse_lazy('login_handler')
    success_message = "User has been deleted successfully."
    template_name = 'delete\delete_user.html'


    def get_object(self):
        messages.success(self.request, self.success_message)
        return get_object_or_404(User, pk=self.request.user.id)
