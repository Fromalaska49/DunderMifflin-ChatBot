# Dictionary Key Value Constants
CHATBOT_MACHINE_STATE = 'CHATBOT_STATE'
LOGIN_ATTEMPTS = 'LOGIN_ATTEMPTS'
RET_CODE = 'RET_CODE'
ERROR = 'ERROR'
EMAIL = 'EMAIL'
INPUT = 'INPUT'
MSG = 'MESSAGE'
USER = 'USER'


# ChatBot State Machine States
ANSWER_VERIFICATION_STATE = 'ANSWER_VERIFICATION_STATE'
LOGGED_IN_AUTH_STATE = 'LOGGED_IN_AUTH_STATE'
AUTHENTICATED_INPUT_STATE = 'QUESTION_STATE'
INFO_UPDATE_STATE = 'INFO_UPDATE_STATE'
INITIAL_STATE = None


# Canned ChatBot Responses That Should Not Require DB Access
ATTEMPTS_EXCEEDED = 'You have exceeded the amount of login attempts. This account has been locked for security reasons.'
ACCOUNT_NOT_VERIFIED = 'Your account has not yet been verified. Please verify your account before logging in.'
COMBINATION_INVALID = 'Invalid email/password combination. try again. Please enter your email:'
LOGIN_SUCCESS = 'Login successful. What can I help you with?'
ENTER_PASSWORD = 'Please enter your password'


# Login State Machine States (Sub-State Machine of ChatBot Machine)
LOGIN_MACHINE_STATE = 'LOGIN_STATE_MACHINE'
USERNAME_STATE = 'USERNAME_STATE'
NULL_STATE = None


# Return Codes
INVALID_CREDENTIALS = 'INVALID_CREDENTIALS'
PASSWORD_REQUIRED = 'PASSWORD_REQUIRED'
ACCOUNT_INACTIVE = 'ACCOUNT_INACTIVE'
ACCOUNT_LOCKED = 'ACCOUNT_LOCKED'
AUTH_SUCCESS = 'AUTH_SUCCESS'
ERROR = 'ERROR'


# Constants Used in General Statements
LOGIN_ATTEMPT_LIMIT = 5
