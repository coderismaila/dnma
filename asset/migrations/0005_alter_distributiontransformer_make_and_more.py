# Generated by Django 4.1.4 on 2022-12-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asset", "0004_alter_distributiontransformer_make_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distributiontransformer",
            name="make",
            field=models.CharField(blank=True, max_length=50, verbose_name="make"),
        ),
        migrations.AlterField(
            model_name="powertransformer",
            name="make",
            field=models.CharField(blank=True, max_length=50, verbose_name="make"),
        ),
    ]