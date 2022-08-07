from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from accounts.common.models import TimeStampedUUIDModel


User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")



class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        User, 
        related_name="profile", 
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        verbose_name=_("Phone Number"), 
        max_length=30, 
        default="+233......"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), 
        default="say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), 
        default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        max_length=20,
    )
    store_owner = models.BooleanField(
        verbose_name='Store Owner',
        default=False,
        help_text='Are you a Store Owner?',
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Address(models.Model):
    profile = models.OneToOneField(
        Profile, 
        on_delete=models.CASCADE
    )
    country = CountryField(
        verbose_name=_("Country"), 
        default="GH", 
        blank=False, 
        null=False
    )
    street = models.CharField(
        max_length=200, 
        blank=True, 
        null=True
    )
    house_number = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    region = models.CharField(
        max_length=50,
        null=False, 
        blank=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Accra",
        blank=False,
        null=False,
    )
    digital_address = models.CharField(
        max_length=15,
            null=False, 
            blank=False
    )


class Measurement(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name='user_measurements'
    )
    neck = models.IntegerField(
        verbose_name='Around neck',
    )
    bust = models.IntegerField(
        verbose_name='Bust area',
    )
    arm_length = models.IntegerField(
        verbose_name='Arm length short',
    )
    long_sleeve = models.IntegerField(
        verbose_name='Arm length long',
    )
    bicep = models.IntegerField(
        verbose_name='Bicep',
    )
    wrist = models.IntegerField(
        verbose_name='Wrist',
    )
    torso = models.IntegerField(
        verbose_name='Torso length',
    )
    waist = models.IntegerField(
        verbose_name='Waist',
    )
    hips = models.IntegerField(
        verbose_name='hips',
    )
    waist_to_above_knee = models.IntegerField(
        verbose_name='Skirt/ Shorts length',
    )
    waist_to_below_knee = models.IntegerField(
        verbose_name='Trouser length',
    )
    calf = models.IntegerField(
        verbose_name='Calf',
    )