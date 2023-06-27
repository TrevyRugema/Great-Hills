from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class MemberManager(BaseUserManager):
    def create_member(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Email Should be Provided')
        email=self.normalize_email(email)
        new_member=self.model(email=email,**extra_fields)
        new_member.set_password(password)
        return new_member
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperMember should have is_super_member ')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser should have is_super_user')
        return self.create_member(email,password,**extra_fields)

class Member(AbstractUser):
    class Role(models.TextChoices):
        PRESIDENT='PRESIDENT','President',
        VISE_PRESIDENT='VISE_PRESIDENT','Vise_President',
        ACCOUNTANT='ACCOUNTANT','ACCOUNTANT',
        ORIDINARY_MEMBER='ORDINARY_MEMBER','Ordinary_Member',
        ADMIN='ADMIN','Admin',
    username=models.CharField(max_length=80,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    mobile_number=PhoneNumberField(null=False,unique=True)
    gender=models.TextChoices('Male','Female')
    address=models.TextField()
    role=models.CharField(_('Role'),max_length=80,choices=Role.choices,default=Role.ORIDINARY_MEMBER)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','mobile_number','role']
    objects=MemberManager()

    def __str__(self):
        return f" {self.first_name}{self.Role}"



