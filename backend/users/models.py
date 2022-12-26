import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

def uuid4():
    return str(uuid.uuid4())

class User(AbstractUser):
    id = models.CharField(primary_key=True, default=uuid4, max_length=36, editable=False)
    email = models.EmailField(unique=True)
    
    
    EMAIL_FIELD: str = 'email'
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list[str] = ['username']
    
    def __str__(self) -> str:
        return self.email
    
    
    class Meta:
        unique_together = ('email', 'username')
        db_table: str = 'users'
        verbose_name: str = 'User'
        verbose_name_plural: str = 'Users'
        ordering: list[str] = ['email']