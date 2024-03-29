import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from ChatBot.views.misc.Constants import *
from ChatBot.views.login.Login import Login
from testing.TestingUtil import print_expected_received, Session
import json
'''Imports and settings configuration MUST be interleaved above'''

URL = LOCALHOST + LOGIN_ENDPT
view = Login.as_view()

class LoginTest:

    @staticmethod
    def test_login_bad_passwd(request_factory):
        incorrect_pass = 'incorr3ctp4ssw0rd'
        params = {
            EMAIL: TEST_USER_EMAIL,
            PASSWORD: incorrect_pass
        }
        request = request_factory.post(URL, params)
        request.session = Session()
        print '\tTesting Login For Test User Using Incorrect Password: ' + incorrect_pass
        response = view(request)
        print_expected_received({ERROR: True, MSG: COMBINATION_INVALID}, response.content)
        response_object = json.loads(response.content)
        return response_object[ERROR] == True and response_object[MSG] == COMBINATION_INVALID

    @staticmethod
    def test_login_account_not_verified(request_factory):
        params = {
            EMAIL: TEST_ADMIN_EMAIL,
            PASSWORD: TEST_PSSWD
        }
        request = request_factory.post(URL, params)
        request.session = Session()
        print '\tTesting Unverified Account Login Using Valid Test Admin Credentials'
        response = view(request)
        print_expected_received({ERROR: True, MSG: ACCOUNT_NOT_VERIFIED}, response.content)
        response_object = json.loads(response.content)
        return response_object[ERROR] == True and response_object[MSG] == ACCOUNT_NOT_VERIFIED

    @staticmethod
    def test_login_success(request_factory):
        params = {
            EMAIL: TEST_USER_EMAIL,
            PASSWORD: TEST_PSSWD
        }
        request = request_factory.post(URL, params)
        request.session = Session()
        print '\tTesting Successful Login Using Verified Test User Account'
        response = view(request)
        print_expected_received({ERROR: False, MSG: LOGIN_SUCCESS}, response.content)
        response_object = json.loads(response.content)
        return response_object[ERROR] == False and response_object[MSG] == LOGIN_SUCCESS
