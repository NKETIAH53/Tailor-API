# Generated by Django 4.0.6 on 2022-08-16 03:22

from django.db import migrations, models
import store_api.models


class Migration(migrations.Migration):

    dependencies = [
        ("store_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=store_api.models.media_uploads,
                verbose_name="design image",
            ),
        ),
    ]
