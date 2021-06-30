from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True,
                              help_text='Email address of user')

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Profile(models.Model):
    """Store information about user"""

    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50,
                                  help_text='First name of user')

    last_name = models.CharField(max_length=50,
                                 help_text='Last name (surname) of user')

    date_of_birth = models.DateField(help_text='Users data of birth',
                                     null=True,
                                     blank=True)

    phone_number = PhoneNumberField(null=True, blank=True,
                                    help_text='Contact number where user can be reached')

    email_address = models.EmailField(max_length=50,
                                      help_text='Email address of user')

    city = models.CharField(max_length=50,
                            help_text='City where user currently resides')

    country = models.CharField(max_length=50,
                               help_text='Country where user currently resides')

    summary = models.TextField(help_text='Short summary describing user')


class Project(models.Model):
    """Relatable project"""

    description = models.CharField(max_length=100,
                                   help_text='Description of project')

    url = models.URLField(help_text='URL to project')

    summary = models.TextField(help_text='Short summary describing project',
                               null=True,
                               blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Experience(models.Model):
    """Store job experience history"""
    user = models.ForeignKey(CustomUser,
                             help_text='Users experience',
                             related_name='experience',
                             on_delete=models.CASCADE)

    title = models.CharField(max_length=50,
                             help_text='Official position name in company')

    company = models.CharField(max_length=50,
                               help_text='Name of company')

    country = models.CharField(max_length=50,
                               help_text='Country where job resided')

    summary = models.TextField(
        help_text='Short summary of experience and responsibilities')

    start_date = models.DateField(help_text='Approximate start date of job')

    end_date = models.DateField(null=True, blank=True,
                                help_text='Approximate end date of job')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"


class Skill(models.Model):
    """Store skills and related frameworks"""

    user = models.ForeignKey(CustomUser,
                             help_text='Users skills',
                             related_name='skills',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=100,
                            help_text='Name of skill, language or framework')

    confidence = models.FloatField(validators=[MinValueValidator(1.0),
                                               MaxValueValidator(10.0)],
                                   help_text='Apprximate confidence rating of skill')

    example = models.ForeignKey(Project,
                                help_text='Related project',
                                related_name='skill',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)

    icon = models.CharField(max_length=50,
                            help_text='Font awesome icon',
                            null=True,
                            blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Education(models.Model):
    """Store education history"""

    user = models.ForeignKey(CustomUser,
                             help_text='Users education',
                             related_name='education',
                             on_delete=models.CASCADE)

    degree = models.CharField(max_length=50,
                              help_text='Name of degree')

    university = models.CharField(max_length=50,
                                  help_text='Name of university where '
                                  'student got degree')

    country = models.CharField(max_length=50,
                               help_text='Country where degree was given')

    summary = models.TextField(null=True, blank=True,
                               help_text='Short summary of experience and '
                               'skills learned during degree')

    example = models.ForeignKey(Project,
                                help_text='Related project',
                                related_name='project',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)

    start_date = models.DateField(
        null=True, blank=True, help_text='Approximate start date of degree')

    end_date = models.DateField(
        null=True, blank=True, help_text='Approximate end date of degree')

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"


class Link(models.Model):
    """Relatable link"""

    user = models.ForeignKey(CustomUser,
                             help_text='User links',
                             related_name='link',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=100,
                                   help_text='Link name')

    url = models.URLField(help_text='Link')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"