import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """
    Defines our custom user class.
    Username, email and password are required.
    """

    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
        )
    
    first_name = models.CharField(max_length=100, null=True, blank=True)

    last_name = models.CharField(max_length=100, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.username

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.first_name
    
    def when_user_joined(self):
        """
        This method is for finding the user joined
        """
        return self.timestamp

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class CustomUserPermissions(models.Model):
    """
    This model gonna handle all the custom permissions that are going to be assigned to each user
    """
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=255, null=True, blank=True, choices = PRIORITY_CHOICES)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

    def __str__(self):
        return self.name



class UserType(models.Model):
    """
    This model is gonna handle the user type and custom permissions handlers
    """
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=255, null=True, blank=True, choices = PRIORITY_CHOICES)
    permissions = models.ManyToManyField(CustomUserPermissions, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'

    def __str__(self):
        return self.name

    
class UserProfile(models.Model):
    """
    This is the model gonna handle the user profile which will be created automatically whenever the user is registered.
    """
    USER_PROFILE_IMAGE = "user_profile_image"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=USER_PROFILE_IMAGE)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.email

    def get_user_type(self):
        return self.user_type.name


class UserDevice(models.Model):
    """
    this table will be updated whenever user logins, storing device information and ip address of the user
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    device_name = models.CharField(max_length=255, null=True, blank=True)
    os = models.CharField(max_length=255, null=True, blank=True)
    browser = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, validators=[validators.validate_ipv4_address,])
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp', 'user', 'device_name')
        verbose_name = 'User Device'
        verbose_name_plural = 'User Devices'

    def __str__(self):
        return self.user.email
