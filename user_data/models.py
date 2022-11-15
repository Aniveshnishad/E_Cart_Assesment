from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from user_data.manager import CustomManager


class UserTable(AbstractUser):
    """customization of default User"""
    username = None
    email = models.EmailField(unique=True)   #r'[A-Za-z0-9@#$%^&+=]{8,20}
    password = models.CharField(max_length=100, null=False, blank=False,
                                validators=[RegexValidator(r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,20}$',
                                                           message='Must have at least one upper case alphabate, one digit, and one special character')])
    first_name = None
    last_name = None
    firstName = models.CharField(max_length=150, validators=[RegexValidator(r"^[a-zA-Z]+$",
                                                                            message='Must use ALPHA CHARACTERS only')])
    lastName = models.CharField(max_length=150, validators=[RegexValidator(r"^[a-zA-Z . '/]+$",
                                                                           message='Must use ALPHA CHARACTERS only')])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects_manager = CustomManager()

    def __str__(self):
        """refer entire class as given user attributes"""
        return self.email
