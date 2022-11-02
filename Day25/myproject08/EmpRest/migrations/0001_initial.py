# Generated by Django 4.1.2 on 2022-11-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Empname", models.CharField(max_length=50)),
                ("Deptname", models.CharField(max_length=50)),
                ("Designation", models.CharField(max_length=50)),
                ("Age", models.IntegerField()),
                ("Salary", models.FloatField()),
            ],
        ),
    ]
