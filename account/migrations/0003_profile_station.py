# Generated by Django 4.1.4 on 2022-12-20 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asset", "0001_initial"),
        ("account", "0002_alter_profile_area_office_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="station",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="asset.station",
            ),
        ),
    ]