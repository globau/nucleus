# Generated by Django 2.2.13 on 2021-10-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rna", "0004_auto_20211005_1522"),
    ]

    operations = [
        migrations.AlterField(
            model_name="release",
            name="channel",
            field=models.CharField(choices=[("Nightly", "Nightly"), ("Beta", "Beta"), ("Release", "Release"), ("ESR", "ESR")], max_length=255),
        ),
    ]
