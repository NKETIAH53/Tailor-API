# Generated by Django 4.0.6 on 2022-08-28 19:03

import accounts.profiles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CommonProfileFields",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="GH", max_length=2, verbose_name="Country"
                    ),
                ),
                ("street", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "house_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("region", models.CharField(max_length=50)),
                (
                    "city",
                    models.CharField(
                        default="Accra", max_length=180, verbose_name="City"
                    ),
                ),
                ("digital_address", models.CharField(max_length=15)),
                (
                    "phone_number",
                    models.CharField(
                        default="+233......", max_length=30, verbose_name="Phone Number"
                    ),
                ),
                (
                    "about_me",
                    models.TextField(
                        default="say something about yourself", verbose_name="About me"
                    ),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        upload_to=accounts.profiles.models.upload_profile_photo,
                        verbose_name="Profile Photo",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("m", "Male"), ("f", "Female")],
                        max_length=10,
                        verbose_name="Gender",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StoreOwnerProfile",
            fields=[
                (
                    "commonprofilefields_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="profiles.commonprofilefields",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("profiles.commonprofilefields",),
        ),
        migrations.CreateModel(
            name="ClientProfile",
            fields=[
                (
                    "commonprofilefields_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="profiles.commonprofilefields",
                    ),
                ),
                (
                    "neck",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Around neck",
                    ),
                ),
                (
                    "bust",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Bust area",
                    ),
                ),
                (
                    "arm_length",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Arm length short",
                    ),
                ),
                (
                    "long_sleeve",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Arm length long",
                    ),
                ),
                (
                    "bicep",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Bicep",
                    ),
                ),
                (
                    "wrist",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Wrist",
                    ),
                ),
                (
                    "torso",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Torso length",
                    ),
                ),
                (
                    "waist",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Waist",
                    ),
                ),
                (
                    "hips",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="hips",
                    ),
                ),
                (
                    "waist_to_above_knee",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Skirt/ Shorts length",
                    ),
                ),
                (
                    "waist_to_below_knee",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Trouser length",
                    ),
                ),
                (
                    "calf",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=2,
                        null=True,
                        verbose_name="Calf",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("profiles.commonprofilefields",),
        ),
    ]
