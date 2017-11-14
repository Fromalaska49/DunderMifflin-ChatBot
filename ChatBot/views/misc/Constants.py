# Dictionary Key Value Constants
LOGIN_MACHINE_STATE = 'LOGIN_STATE_MACHINE'
CHATBOT_MACHINE_STATE = 'CHATBOT_MACHINE_STATE'
LOGIN_ATTEMPTS = 'LOGIN_ATTEMPTS'
RET_CODE = 'RET_CODE'
ERROR = 'ERROR'
EMAIL = 'EMAIL'
INPUT = 'INPUT'
MSG = 'MESSAGE'
USER = 'USER'


# ChatBot State Machine States
INQUIRY_VERIFICATION_STATE = 'INQUIRY_VERIFICATION_STATE'
ACCOUNT_RECOVERY_STATE = 'ACCOUNT_RECOVERY_STATE'
PASSWORD_UPDATE_STATE = 'PASSWORD_UPDATE_STATE'
AUTHENTICATION_STATE = 'AUTHENTICATION_STATE'
EMAIL_UPDATE_STATE = 'EMAIL_UPDATE_STATE'
NAME_UPDATE_STATE = 'INFO_UPDATE_STATE'
INQUIRE_STATE = 'INQUIRE_STATE'
LOGIN_STATE = 'LOGIN_STATE'
INITIAL_STATE = None

# Canned ChatBot Responses That Should Not Require DB Access
ATTEMPTS_EXCEEDED = 'You have exceeded the amount of login attempts. This account has been locked for security reasons.'
INITIAL_HELP = 'Sorry, I was unable to recognize your input. You may request login or may request account recovery'
ACCOUNT_NOT_VERIFIED = 'Your account has not yet been verified. Please verify your account before logging in.'
COMBINATION_INVALID = 'Invalid email/password combination. try again. Please enter your email:'
LOGIN_SUCCESS = 'Login successful. What can I help you with?'
ENTER_PASSWORD = 'Please enter your password'
ENTER_EMAIL = 'Please enter your email'

# Login State Machine States (Sub-State Machine of ChatBot Machine)
EMAIL_STATE = 'EMAIL_STATE'
NULL_STATE = None


# Return Codes
INVALID_CREDENTIALS = 'INVALID_CREDENTIALS'
PASSWORD_REQUIRED = 'PASSWORD_REQUIRED'
ACCOUNT_INACTIVE = 'ACCOUNT_INACTIVE'
ACCOUNT_LOCKED = 'ACCOUNT_LOCKED'
AUTH_SUCCESS = 'AUTH_SUCCESS'
AMBIGUOUS = 'AMBIGUOUS'
ERROR = 'ERROR'


# Constants Used in General Statements
LOGIN_ATTEMPT_LIMIT = 5
