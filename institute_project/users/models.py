from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    
    USER_TYPES = [
        ('Admin', 'Admin' ),
        ('Teacher', 'Teacher' ),
        ('Student', 'Student' )
    ]
    
    user_type = models.CharField(choices=USER_TYPES, max_length=20, null=True)
    
    def __str__(self):
        return f'{self.username}'
    
    
