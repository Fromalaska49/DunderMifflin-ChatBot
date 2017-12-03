import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ChatBot.views.misc.Constants import *
from ChatBot.views.registration.UserRegistration import UserRegistration
from django.utils.crypto import get_random_string
import json
'''Do Not Change Import Order'''

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

    @staticmethod
    def test_registration_blank_lname(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "SomePasswd123!@#",
            CONFIRM_PASSWORD: "SomePasswd123!@#",
            FIRST_NAME: "Max",
            LAST_NAME: ""
        }
        print "\tTesting Registration Using Blank Last Name"
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: LNAME_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == LNAME_ERROR

    @staticmethod
    def test_registration_bad_psswd_digits(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "SomePasswd!@#",
            CONFIRM_PASSWORD: "SomePasswd!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Password That Fails Digit Requirements: " + params[PASSWORD]
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: PASS_NUMBER_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == PASS_NUMBER_ERROR

    @staticmethod
    def test_registration_bad_psswd_uppercase(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "somepasswd123!@#",
            CONFIRM_PASSWORD: "somepasswd123!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Password That Fails Uppercase Requirements: " + params[PASSWORD]
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: PASS_UPPERCASE_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == PASS_UPPERCASE_ERROR

    @staticmethod
    def test_registration_bad_psswd_symbols(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "SomePasswd123",
            CONFIRM_PASSWORD: "SomePasswd123",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Password That Fails Symbol Requirements: " + params[PASSWORD]
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: PASS_SYMBOL_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == PASS_SYMBOL_ERROR

    @staticmethod
    def test_registration_bad_psswd_match(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "SomePasswd123!@#",
            CONFIRM_PASSWORD: "SomePasswd456!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Passwords That Do Not Match: " + params[PASSWORD] + " " + params[CONFIRM_PASSWORD]
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: PASS_MATCH_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == PASS_MATCH_ERROR

    @staticmethod
    def test_registration_bad_psswd_length(request_factory):
        params = params = {
            EMAIL: "hello@maillinator.com",
            PASSWORD: "SoP12!@",
            CONFIRM_PASSWORD: "SoP12!@",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Registration Using Password That Is Too Short: " + params[PASSWORD]
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: True, MSG: PASS_LENGTH_ERROR}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == True and response_object[MSG] == PASS_LENGTH_ERROR

    @staticmethod
    def test_registration_chatbot_user_success(request_factory):
        random_email = 'randomgen' + get_random_string() + '@mailinator.com'
        params = params = {
            EMAIL: random_email,
            PASSWORD: "SomePassword123!@#",
            CONFIRM_PASSWORD: "SomePassword123!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus"
        }
        print "\tTesting Successful ChatBot User Registration Using Random Email: " + random_email + \
              "\n\tCreates Account and Sends Verification Email (Email Transporting May Take a Few Moments...)"
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: False, MSG: CREATED_USER}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == False and response_object[MSG] == CREATED_USER

    @staticmethod
    def test_registration_admin_user_success(request_factory):
        random_email = 'randomgen' + get_random_string() + '@mailinator.com'
        params = params = {
            EMAIL: random_email,
            PASSWORD: "SomePassword123!@#",
            CONFIRM_PASSWORD: "SomePassword123!@#",
            FIRST_NAME: "Max",
            LAST_NAME: "Pegasus",
            ACCOUNT_TYPE: ADMIN
        }
        print "\tTesting Successful Admin User Registration Using Random Email: " + random_email + \
              "\n\tCreates Account and Sends Verification Email to OIT for Admin Account Confirmation. " \
              "\n\tDevelopment OIT email: " + OIT_EMAIL + \
              "\n\t(Email Transporting May Take a Few Moments...)"
        request = request_factory.post(URL, params)
        response = view(request)
        print_expected_received({ERROR: False, MSG: CREATED_ADMIN}, response.content)
        response_object = json.loads(response.content)

        return response_object[ERROR] == False and response_object[MSG] == CREATED_ADMIN

