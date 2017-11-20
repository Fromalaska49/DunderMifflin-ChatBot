from django.db import models
from django.contrib.auth.models import User as AuthUser

# This is the section where database tables are defined in the form of class definitions (where ORM starts)


class User(AuthUser):
    is_locked = models.BooleanField(default=False)
    acct_locked_token = models.CharField(max_length=12, default="")
    acct_verification_token = models.CharField(max_length=12, default="")

