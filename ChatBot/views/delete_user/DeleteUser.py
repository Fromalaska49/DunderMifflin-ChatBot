import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ChatBot import models
from ChatBot.views.misc.Constants import DELETE_SUCCESS


class DeleteUser(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    # gets instance of user and allows for only authorized
    # deletions. User must be logged in
    model = models.User
    success_url = reverse_lazy('registration')
    success_message = DELETE_SUCCESS
    template_name = 'delete/delete_user.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteUser, self).delete(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
