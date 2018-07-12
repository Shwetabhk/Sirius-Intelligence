from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
import random
import os

class UserManager(BaseUserManager):
    def create_user(self, email,username,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password,username):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password,username):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

def get_file_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

#Renaming the image file to truck+(Random Integer)
def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    name_ins=str(instance).split('@')[0]
    name,ext=get_file_ext(filename)
    return "ProfilePics/{name}{ext}".format(name=name_ins,ext=ext)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True,verbose_name='email address')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    picture = models.ImageField(upload_to=upload_image_path,null=True)
    username = models.CharField(max_length=100,unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']
    object = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
