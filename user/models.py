<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUserModel(AbstractUser):
    token = models.CharField(max_length=100,default = 0 )
    verified = models.BooleanField(default=False)
=======
from django.db import models

# Create your models here.
>>>>>>> 0204819d1d498b7bd2a63d076d99142d295311fc
