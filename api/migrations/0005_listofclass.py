# Generated by Django 4.2.3 on 2023-08-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_recipe_alter_listofallmodel_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="ListofClass",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("class_id", models.IntegerField()),
            ],
        ),
    ]