# Generated by Django 4.2.3 on 2023-08-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_remove_recipe_fuzzclassquery_remove_recipe_dish_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="dish_info",
            field=models.CharField(max_length=256, null=True, verbose_name="简介"),
        ),
    ]