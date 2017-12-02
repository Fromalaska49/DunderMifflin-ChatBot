import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ChatBot.views.misc.Constants import *
from ChatBot.views.registration.UserRegistration import UserRegistration
import json

URL = LOCALHOST + REGISTRATION_ENDPT
view = UserRegistration.as_view()


def print_expected_received(expected_obj, json_received):
    print "\tExpected: " + json.dumps(expected_obj)
    print "\tReceived: " + json_received


class RegistrationTest:

    @staticmethod
    def test_registration_blank_email(request_factory):
        params = params = {
            EMAIL: "",
            PASSWORD: "SomePasswd123!@#",
            CONFIRM_PASSWORD: "SomePasswd123!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration With Blank Email"
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: EMAIL_INVALID_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == EMAIL_INVALID_ERROR

    @staticmethod
    def test_registration_bad_email(request_factory):
        params = params = {
            EMAIL: "hello@bademail",
            PASSWORD: "SomePasswd123!@#",
            CONFIRM_PASSWORD: "SomePasswd123!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Email: " + params[EMAIL] + " (Bad Email)"
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: EMAIL_INVALID_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == EMAIL_INVALID_ERROR


    @staticmethod
    def test_registration_blank_fname(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "SomePasswd123!@#",
            CONFIRM_PASSWORD: "SomePasswd123!@#",
            FIRST_NAME: "",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Blank First Name"
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: FNAME_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == FNAME_ERROR
