# Generated by Django 4.2.3 on 2023-09-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0025_material_img_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("class_id", models.IntegerField()),
                ("class_name", models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name="ListofClass",
        ),
    ]
