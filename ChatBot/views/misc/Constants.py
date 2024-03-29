# Dictionary Key Value Constants
CONFIRM_PASSWORD = 'CONFIRM_PASSWORD'
OLD_PASSWORD = 'OLD_PASSWORD'
NEW_PASSWORD = 'NEW_PASSWORD'
PASS_RESET_TOKEN = 'PASS_RESET_TOKEN'
PASS_CHANGE_TOKEN = 'PASS_CHANGE_TOKEN'
LOGIN_ATTEMPTS = 'LOGIN_ATTEMPTS'
ACCOUNT_TYPE = 'ACCOUNT_TYPE'
CHANGE_TYPE = 'CHANGE_TYPE'
FIRST_NAME = 'FIRST_NAME'
HTTP_HOST = 'HTTP_HOST'
HTTP_PREFIX = 'http://'
LAST_NAME = 'LAST_NAME'
RET_CODE = 'RET_CODE'
PASSWORD = 'PASSWORD'
ERROR = 'ERROR'
EMAIL = 'EMAIL'
INPUT = 'INPUT'
MSG = 'MESSAGE'
ADMIN = 'ADMIN'
USER = 'USER'
QUESTION_TEXT = 'QUESTION_TEXT'
INTENT_ID = 'INTENT_ID'
INTENT_NAME = 'INTENT_NAME'
INTENT_USER_SAYS = 'INTENT_USER_SAYS'
INTENT_RESPONSE = 'INTENT_RESPONSE'

# Used in Testing
NUM_PASS = 'NUM_PASS'
NUM_FAIL = 'NUM_FAIL'
TEST_VERIF_TOKEN = 'ACNENWOIRNBY'

# Toy UTSA OIT Email
OIT_EMAIL = 'oitutsa@mailinator.com'

# Toy ChatBot system email
CHATBOT_EMAIL = 'chatbotutsa@mailinator.com'

# Canned ChatBot Responses That Should Not Require DB Access
ATTEMPTS_EXCEEDED = 'You have exceeded the maximum number of login attempts. This account has been locked for security reasons. ' \
                    'An email has been sent to this account\'s email address with instructions for unlocking this account.'
CREATED_ADMIN = 'Your account has been successfully created and will become active once an OIT staff member activates it. Please check your email and click the link to verify your email.'
ACCOUNT_IS_LOCKED = 'Your account has been locked for security reasons. Please check you email for instructions on ' \
                    'unlocking this account.'
PASS_RESET_REQ_SUCCESS = 'An email with password reset instructions will be sent to the email address provided if an account' \
                     ' with that email address exists.'
ACCOUNT_NOT_VERIFIED = 'Your account has not yet been verified. Please verify your account before logging in.'
CREATED_USER = 'Your account has been successfully created. Please check your email to activate your account.'
COMBINATION_INVALID = 'The email or password was incorrect.'
PASS_RESET_SUCCESS = 'Your password has been successfully updated.'
LOGIN_SUCCESS = 'Login successful. What can I help you with?'
DELETE_SUCCESS = 'Your account has been deleted.'
UPDATE_SUCCESS = 'Your user profile has been updated'
PASS_CHANGE_SUCCESS = 'Your password has been changed successfully'
ENTER_PASSWORD = 'Please enter your password.'
INCORRECT_PARAMETERS = 'Incorrect parameters'
ENTER_EMAIL = 'Please enter your email.'

# Constants Used in General Statements
LOGIN_ATTEMPT_LIMIT = 5
TEST_USER_EMAIL = 'chatbotUserTestEmail__@mailinator.com'
TEST_PSSWD = 'SomePassword123!@#'
TEST_ADMIN_EMAIL = 'chatbotAdminTestEmail__@mailinator.com'

# Password Constraint Messages
PASS_UPPERCASE_ERROR = 'Your password must contain at least two uppercase letters'
PASS_SYMBOL_ERROR = 'Your password must contain at least two of the following characters: ! @ # $ % & * - +'
PASS_NUMBER_ERROR = 'Your password must contain at least two digits'
PASS_LENGTH_ERROR = 'Your password must be at least 8 characters long'
PASS_MATCH_ERROR = 'Your passwords do not match'

# Email Error Messages
EMAIL_TAKEN_ERROR = 'This email is already in use'
EMAIL_INVALID_ERROR = 'You must provide a valid email address'

# Name Error Messages
FNAME_ERROR = 'Please enter a first name'
LNAME_ERROR = 'Please enter a last name'

# Localhost
LOCALHOST = '127.0.0.1:8000'

# Endpoints
REGISTRATION_ENDPT = '/registration'
VERIFICATION_ENDPT = '/verify'
LOGIN_ENDPT = '/login'

# API.AI client key
API_CLIENT_KEY = '8f652156aa8a434daaf9e9d3eb174313'
API_DEV_KEY = '670486e053a84bd88285c0b3f03cddcb'

# API.AI URL
API_URL = 'https://api.dialogflow.com/v1/intents'
API_URL_TAIL = '?v=20150910&lang=en'
API_HEADER = {"Content-Type": "application/json", "Authorization": "Bearer 670486e053a84bd88285c0b3f03cddcb"}
