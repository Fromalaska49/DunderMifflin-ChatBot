from django.db import models
from django.contrib.auth.models import User as AuthUser

# This is the section where database tables are defined in the form of class definitions (where ORM starts)


class User(AuthUser):
    acct_active = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    pass_reset_token = models.CharField(max_length=12, default="")
    pass_reset_token_stamp = models.DateTimeField(null=True)
    acct_locked_token = models.CharField(max_length=12, default="")
    acct_locked_token_stamp = models.DateTimeField(null=True)
    acct_verification_token = models.CharField(max_length=12, default="")
    acct_verification_token_stamp = models.DateTimeField(null=True)

