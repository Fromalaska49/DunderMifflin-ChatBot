from django.core.mail import send_mail
from ChatBot.views.misc.Constants import *


def send_welcome_email(email, host, token):
    link = 'http://' + host + '/verify/' + token
    send_mail('Your New ChatBotAccount', 'You have created a new chatbot account. '
                                         'You may activate this account by clicking '
                                         'on this link: ' + link, CHATBOT_EMAIL, [email])


def send_admin_verification_email(fname, lname, email, host, token):
    link = 'http://' + host + '/verify/' + token
    send_mail('ChatBot Administrator Account Creation',
              'A ChatBot administrator account has been created using the following information:\n\n'
              'First Name:\t' + fname + '\n'
              'Last Name:\t' + lname + '\n'
              'Email:\t' + email + '\n\n'
              'You may activate this account by clicking on the following link: ' + link + ' \n'
              'Otherwise, you may ignore this email. The verification link will expire in 72 hours.',
              CHATBOT_EMAIL,
              [OIT_EMAIL])


def send_account_locked_email(email, host, token):
    link = 'http://' + host + '/unlock/' + token
    send_mail('Your ChatBot Account Has Been Locked', 'Your account has been locked. '
                                                      'You may unlock your account by clicking '
                                                      'on this link: ' + link, CHATBOT_EMAIL, [email])


def send_admin_verified_email(email, host):
    send_mail('ChatBot Administrator Account Activated',
              'Your ChatBot Administrator account has been'
              'successfully activated by UTSA OIT Personnel.',
              CHATBOT_EMAIL,
              [email])


def send_pass_reset_email(email, host, token):
    link = 'http://' + host + '/reset/' + token
    send_mail('Reset Your ChatBot Account Password',
              'You have indicated that you would like to reset your password. '
              'You may reset your password by clicking '
              'on this link: ' + link, CHATBOT_EMAIL, [email])

