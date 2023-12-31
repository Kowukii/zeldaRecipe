# Generated by Django 4.2.3 on 2023-07-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserModel",
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
                ("material_name", models.CharField(max_length=30, unique=True)),
                ("material_region", models.CharField(max_length=30)),
                ("material_feature", models.CharField(max_length=30)),
                ("material_info", models.CharField(max_length=128)),
                ("food_name", models.CharField(max_length=30)),
                ("food_recipe", models.CharField(max_length=30)),
                ("food_feature", models.CharField(max_length=30)),
            ],
        ),
    ]
