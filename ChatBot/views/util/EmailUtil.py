from django.core.mail import send_mail


def send_welcome_email(email):
    send_mail('Your New ChatBotAccount', 'You have created a new chatbot account.', 'oit@utsa.edu', [email])


def send_account_locked_email(email):
    send_mail('Your ChatBot Account Has Been Locked', 'Your account has been locked.', 'oit@utsa.edu', [email])
