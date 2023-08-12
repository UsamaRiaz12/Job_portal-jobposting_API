# Generated by Django 4.1.5 on 2023-08-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "em_register",
            "0005_remove_em_register_degree_remove_em_register_email_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="em_register",
            name="email",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="company_name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="date",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="description",
            field=models.TextField(default="", max_length=500),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="job_tittle",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="requirments",
            field=models.TextField(default="", max_length=500),
        ),
    ]
