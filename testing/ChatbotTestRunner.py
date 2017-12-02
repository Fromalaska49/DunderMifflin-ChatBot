import sys
import os.path
import django
from django.conf import settings
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ChatBot import settings as chatbot_settings
settings.configure(default_settings=chatbot_settings, DEBUG=True)
django.setup()
from rest_framework.test import APIRequestFactory
from testing.RegistrationTest import RegistrationTest
import inspect
'''Imports and settings configuration MUST be interleaved above'''

NUM_PASS = 'NUM_PASS'
NUM_FAIL = 'NUM_FAIL'


def determine_result(test_result):
    if test_result is True:
        print '\tPASS!\n'
        total_results[NUM_PASS] += 1
    else:
        print '\tFAIL!\n'
        total_results[NUM_FAIL] += 1


# Runs the static methods defined in a test class. Methods must be static in order for this method to find them
def run_test_class(test_class):
    # method_struct contains method name at index 0 and actual method at index 1
    for method_struct in inspect.getmembers(test_class, predicate=inspect.isfunction):
        print '\tRunning Test: ' + method_struct[0]  # print test name
        result = method_struct[1](request_factory)  # run test method
        determine_result(result)

# Create request factory for testing and define object to hold final results
request_factory = APIRequestFactory()
total_results = {
    NUM_PASS: 0,
    NUM_FAIL: 0
}

print 'Testing Registration Functionality\n'
run_test_class(RegistrationTest)

print 'Total Tests Passed: ' + str(total_results[NUM_PASS])
print 'Total Tests Failed: ' + str(total_results[NUM_FAIL])
