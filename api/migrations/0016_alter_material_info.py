# Generated by Django 4.2.3 on 2023-08-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0015_material"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="info",
            field=models.CharField(max_length=256, verbose_name="简介"),
        ),
    ]
