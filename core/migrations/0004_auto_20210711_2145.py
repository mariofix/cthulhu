# Generated by Django 3.2.5 on 2021-07-12 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_coreuser_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="coreuser",
            name="tz",
            field=models.CharField(
                default="America/Santiago", max_length=255, verbose_name="timezone"
            ),
        ),
        migrations.AlterField(
            model_name="coreuser",
            name="country",
            field=models.CharField(default="CL", max_length=3, verbose_name="country"),
        ),
    ]
