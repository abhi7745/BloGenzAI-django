# Generated by Django 4.1 on 2023-09-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("admin", "Admin"), ("user", "Recruiter")],
                max_length=50,
                null=True,
            ),
        ),
    ]
