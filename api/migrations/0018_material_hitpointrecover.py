# Generated by Django 4.2.3 on 2023-08-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_alter_material_pouchgettype"),
    ]

    operations = [
        migrations.AddField(
            model_name="material",
            name="HitPointRecover",
            field=models.IntegerField(default=0),
        ),
    ]
