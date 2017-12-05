import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from ChatBot.views.misc.Constants import *
from ChatBot.views.account_management.VerifyAccount import VerifyAccount
from testing.TestingUtil import Session
'''Imports and settings configuration MUST be interleaved above'''

URL = LOCALHOST + VERIFICATION_ENDPT


class VerificationTest:

    @staticmethod
    def test_verification_success(request_factory):
        request = request_factory.get(URL + "/" + TEST_VERIF_TOKEN)
        request.session = Session()
        expected = 'Status code: 302 (Redirection) Url: /login'
        print '\tTesting Successful Verification For Test User Using Test Token: ' + TEST_VERIF_TOKEN

        # Test get method directly
        response = VerifyAccount().get(request, TEST_VERIF_TOKEN)

        # successful verification should redirect to login page
        print '\tExpected: ' + expected
        print '\tReceived: Status code: ' + str(response.status_code) + ' Url: ' + response.url

        return response.status_code == 302 and response.url == '/login'
