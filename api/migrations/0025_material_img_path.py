# Generated by Django 4.2.3 on 2023-08-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0024_alter_recipe_dish_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="material",
            name="img_path",
            field=models.CharField(default=" ", max_length=64, verbose_name="img路径"),
        ),
    ]