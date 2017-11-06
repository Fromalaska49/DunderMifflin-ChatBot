from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
import json


#Class-based view (Django calls handlers views)
class Register(ListView):

    #post request handler
    def post(self, request):
        response_data = {}

        if User.objects.filter(email=request.POST['email']).exists():
            response_data['error'] = True
            response_data['msg'] = 'email already taken'

        elif request.POST['password'] != request.POST['confirm-password']:
            response_data['error'] = True
            response_data['msg'] = 'passwords do not match'

        else:
            user = User.objects.create_user(
                                            first_name=request.POST['first-name'],
                                            last_name=request.POST['last-name'],
                                            email=request.POST['email'],
                                            password=request.POST['password'],
                                            username=request.POST['email']              #Django default user table requires username
                                            )

            user.save()
            response_data['error'] = False

        return HttpResponse(json.dumps(response_data), content_type="application/json")


    #get request handler
    def get(self, request):

        #serve registration registration. give path relative to templates folder
        return render(request, "registration/registration.html")

