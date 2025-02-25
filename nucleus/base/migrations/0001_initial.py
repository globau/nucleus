# Generated by Django 2.2.10 on 2020-03-24 22:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="GithubLog",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(blank=True, db_index=True, editable=False)),
                ("object_id", models.PositiveIntegerField()),
                ("branch", models.CharField(default="master", max_length=100)),
                ("ack", models.BooleanField(default=False)),
                ("fail_count", models.PositiveSmallIntegerField(default=0)),
                ("author", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ("content_type", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="contenttypes.ContentType")),
            ],
            options={
                "ordering": ["-created"],
                "get_latest_by": "created",
            },
        ),
    ]
