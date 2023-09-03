# Generated by Django 4.2.3 on 2023-08-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_listofall_delete_listofallmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="ListOfEffect",
            fields=[
                ("effect_id", models.IntegerField(primary_key=True, serialize=False)),
                ("effect_name", models.CharField(max_length=16, verbose_name="类名称")),
            ],
        ),
        migrations.RenameField(
            model_name="listofclass",
            old_name="id",
            new_name="item_id",
        ),
    ]
