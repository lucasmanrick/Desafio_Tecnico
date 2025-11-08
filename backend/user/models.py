from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
from django.utils.timezone import now

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=now, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email