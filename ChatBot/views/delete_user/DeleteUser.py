from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView


# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import render
#
# from ChatBot.views.misc.Constants import ERROR
from ChatBot import models


class DeleteUser(DeleteView):
    #gets instance of user and allows for only authorized
    #deletions. User must be logged in
    model = models.User
    success_url = reverse_lazy('login_handler')
    template_name = 'delete\delete_user.html'


    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
