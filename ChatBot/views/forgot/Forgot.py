from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
import json


# Class-based view (Django calls handlers views)
class Forgot(ListView):

    # Post Request Handler
    def post(self, request):

        return render(request, "forgot.html")
    
    # Get Request Handler
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/chatbot")
        return render(request, "forgot.html")

