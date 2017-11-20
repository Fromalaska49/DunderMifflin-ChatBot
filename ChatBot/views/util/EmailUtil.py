from django.core.mail import send_mail


def send_welcome_email(email, host, token):
    link = 'http://' + host + '/verify/' + token
    send_mail('Your New ChatBotAccount', 'You have created a new chatbot account. '
                                         'You may activate this account by clicking '
                                         'on this link: ' + link, 'oit@utsa.edu', [email])


def send_account_locked_email(email, host, token):
    link = 'http://' + host + '/unlock/' + token
    send_mail('Your ChatBot Account Has Been Locked', 'Your account has been locked. '
                                                      'You may unlock your account by clicking '
                                                      'on this link: ' + link, 'oit@utsa.edu', [email])


