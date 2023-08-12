# Generated by Django 4.1.5 on 2023-08-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("em_register", "0004_em_register_name2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="em_register",
            name="degree",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="email",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="name",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="name2",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="resume",
        ),
        migrations.AddField(
            model_name="em_register",
            name="company_name",
            field=models.CharField(default="usama", max_length=100),
        ),
        migrations.AddField(
            model_name="em_register",
            name="date",
            field=models.CharField(default=-2000, max_length=100),
        ),
        migrations.AddField(
            model_name="em_register",
            name="description",
            field=models.TextField(default="usama", max_length=500),
        ),
        migrations.AddField(
            model_name="em_register",
            name="job_tittle",
            field=models.CharField(default="usama", max_length=100),
        ),
        migrations.AddField(
            model_name="em_register",
            name="requirments",
            field=models.TextField(default="usama", max_length=500),
        ),
    ]
