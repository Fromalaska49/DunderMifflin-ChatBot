# Dictionary Key Value Constants
LOGIN_MACHINE_STATE = 'LOGIN_STATE_MACHINE'
CHATBOT_MACHINE_STATE = 'CHATBOT_MACHINE_STATE'
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

# Toy UTSA OIT Email
OIT_EMAIL = 'oitutsa@mailinator.com'

# Toy ChatBot system email
CHATBOT_EMAIL = 'chatbotutsa@mailinator.com'

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
ATTEMPTS_EXCEEDED = 'You have exceeded the amount of login attempts. This account has been locked for security reasons. ' \
                    'An email has been sent to this account\'s email address with instructions on ulocking this account'
CREATED_ADMIN = 'Your account has been sucessfully created and will become active once an OIT staff member activates it'
ACCOUNT_IS_LOCKED = 'Your account has been locked for security reasons. Please check you email for instructions on ' \
                    'unlocking this account.'
PASS_RESET_REQ_SUCCESS = 'An email with password reset instructions will be sent to the email address provided if an account' \
                     ' with that email address exists'
INITIAL_HELP = 'Sorry, I was unable to recognize your input. You may request login or may request account recovery'
ACCOUNT_NOT_VERIFIED = 'Your account has not yet been verified. Please verify your account before logging in'
CREATED_USER = 'Your account has been successfully created. Please check your email to activate your account'
COMBINATION_INVALID = 'Invalid email/password combination. try again. Please enter your email:'
PASS_RESET_SUCCESS = 'Your password has been successfully updated'
LOGIN_SUCCESS = 'Login successful. What can I help you with?'
ENTER_PASSWORD = 'Please enter your password'
INCORRECT_PARAMETERS = 'Incorrect parameters'
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


# Password Constraint Messages
PASS_UPPERCASE_ERROR = 'Your password must contain at least two uppercase letters'
PASS_SYMBOL_ERROR = 'Your password must contain at least two of the following characters: ! @ # $ % & * - +'
PASS_NUMBER_ERROR = 'Your password must contain at least two digits'
PASS_LENGTH_ERROR = 'Your password must be at least 8 characters long'
PASS_MATCH_ERROR = 'Your passwords do not match'

#Email Error Messages
EMAIL_TAKEN_ERROR = 'This email is already in use'
EMAIL_INVALID_ERROR = 'You must provide a valid email address'

#Name Error Messages
FNAME_ERROR = 'Please enter a first name'
LNAME_ERROR = 'Please entere a last name'
