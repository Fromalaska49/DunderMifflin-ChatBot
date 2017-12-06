import os.path
import sys

import django
from django.conf import settings

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ChatBot import settings as chatbot_settings
settings.configure(default_settings=chatbot_settings, DEBUG=True)
django.setup()
from TestingUtil import *
from rest_framework.test import APIRequestFactory
from testing.test_classes.RegistrationTest import RegistrationTest
from testing.test_classes.VerificationTest import VerificationTest
from testing.test_classes.LoginTest import LoginTest
from ChatBot.models import User
'''Imports and settings configuration MUST be interleaved above'''


# Create request factory for testing and define object to hold final results
request_factory = APIRequestFactory()
total_results = {
    NUM_PASS: 0,
    NUM_FAIL: 0
}
# Delete test accounts that may have been created by previous run of ChatBotTestRunner
delete_test_admin()
delete_test_user()

# Test Registration Functionality. This MUST run first as it creates the test accounts that will be used by later tests
print 'Testing Registration Functionality\n'
run_test_class(RegistrationTest, request_factory, total_results)

# Get test_user account created by RegistrationTest class, set verification token to TEST_VERIF_TOKEN for easy testing
test_user = User.objects.get(email=TEST_USER_EMAIL)
test_user.acct_verification_token = TEST_VERIF_TOKEN
test_user.save()

# Test Account Verification Functionality
run_test_class(VerificationTest, request_factory, total_results)

# Test Login Functionality. This MUST run after the registration and verification test classes
run_test_class(LoginTest, request_factory, total_results)

print 'Total Tests Passed: ' + str(total_results[NUM_PASS])
print 'Total Tests Failed: ' + str(total_results[NUM_FAIL])

