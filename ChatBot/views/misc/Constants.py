# Dictionary Key Value Constants
CONFIRM_PASSWORD = 'CONFIRM_PASSWORD'
PASS_RESET_TOKEN = 'PASS_RESET_TOKEN'
LOGIN_ATTEMPTS = 'LOGIN_ATTEMPTS'
ACCOUNT_TYPE = 'ACCOUNT_TYPE'
CHANGE_TYPE = 'CHANGE_TYPE'
FIRST_NAME = 'FIRST_NAME'
HTTP_HOST = 'HTTP_HOST'
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

# Toy UTSA OIT Email
OIT_EMAIL = 'oitutsa@mailinator.com'

# Toy ChatBot system email
CHATBOT_EMAIL = 'chatbotutsa@mailinator.com'


# Canned ChatBot Responses That Should Not Require DB Access
ATTEMPTS_EXCEEDED = 'You have exceeded the amount of login attempts. This account has been locked for security reasons. ' \
                    'An email has been sent to this account\'s email address with instructions on ulocking this account'
CREATED_ADMIN = 'Your account has been sucessfully created and will become active once an OIT staff member activates it'
ACCOUNT_IS_LOCKED = 'Your account has been locked for security reasons. Please check you email for instructions on ' \
                    'unlocking this account.'
PASS_RESET_REQ_SUCCESS = 'An email with password reset instructions will be sent to the email address provided if an account' \
                     ' with that email address exists'
ACCOUNT_NOT_VERIFIED = 'Your account has not yet been verified. Please verify your account before logging in'
CREATED_USER = 'Your account has been successfully created. Please check your email to activate your account'
COMBINATION_INVALID = 'Invalid email/password combination. try again. Please enter your email:'
PASS_RESET_SUCCESS = 'Your password has been successfully updated'
LOGIN_SUCCESS = 'Login successful. What can I help you with?'
ENTER_PASSWORD = 'Please enter your password'
INCORRECT_PARAMETERS = 'Incorrect parameters'
ENTER_EMAIL = 'Please enter your email'


# Constants Used in General Statements
LOGIN_ATTEMPT_LIMIT = 5


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
LNAME_ERROR = 'Please entere a last name'


# API.AI client key
API_KEY = '8f652156aa8a434daaf9e9d3eb174313'
