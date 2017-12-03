import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from ChatBot.views.misc.Constants import *
from ChatBot.views.account_management.VerifyAccount import VerifyAccount
import json
'''Imports and settings configuration MUST be interleaved above'''

URL = LOCALHOST + VERIFICATION_ENDPT


class VerificationTest:

    @staticmethod
    def test_verification_success(request_factory):
        request = request_factory.get(URL + "/" + TEST_VERIF_TOKEN)
        request.session = {}
        expected = 'Account successfully activated!'
        print '\tTesting Successful Verification using Test Token: ' + TEST_VERIF_TOKEN

        # Test get method directly
        response = VerifyAccount().get(request, TEST_VERIF_TOKEN)
        content = response.content.strip()
        print '\tExpected: ' + expected
        print '\tReceived: ' + content

        return expected == content
