# Generated by Django 4.2.3 on 2023-08-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_recipe_ingrefour_class_id_recipe_ingreone_class_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="dish_name",
            field=models.CharField(max_length=32, verbose_name="食谱名称"),
        ),
    ]
