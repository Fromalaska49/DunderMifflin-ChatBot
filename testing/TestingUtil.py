import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ChatBot.views.misc.Constants import *
from django.contrib.auth.models import User as AuthUser
import inspect
import json


def print_expected_received(expected_obj, json_received):
    print "\tExpected: " + json.dumps(expected_obj)
    print "\tReceived: " + json_received


def determine_result(test_result, total_results):
    if test_result is True:
        print '\tPASS!\n'
        total_results[NUM_PASS] += 1
    else:
        print '\tFAIL!\n'
        total_results[NUM_FAIL] += 1


# Runs the static methods defined in a test class. Methods must be static in order for this method to find them
def run_test_class(test_class, request_factory, total_results):
    # method_struct contains method name at index 0 and actual method at index 1
    for method_struct in inspect.getmembers(test_class, predicate=inspect.isfunction):
        print '\tRunning Test: ' + method_struct[0]  # print test name
        result = method_struct[1](request_factory)  # run test method
        determine_result(result, total_results)


def __delete_account(email):
    if AuthUser.objects.filter(email=email).exists():
        user = AuthUser.objects.get(email=email)
        user.delete()


def delete_test_user():
    __delete_account(TEST_USER_EMAIL)


def delete_test_admin():
    __delete_account(TEST_ADMIN_EMAIL)


class Session(dict):
    modified = None
