# Generated by Django 4.2.3 on 2023-08-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_listofclass"),
    ]

    operations = [
        migrations.CreateModel(
            name="ListOfAll",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("item_name", models.CharField(max_length=8, verbose_name="名称")),
                ("item_name_cn", models.CharField(max_length=8, verbose_name="cn名称")),
                ("class_id", models.IntegerField()),
                ("class_name", models.CharField(max_length=16, verbose_name="类名称")),
                ("info", models.CharField(max_length=32, verbose_name="简介")),
                ("effect_id", models.IntegerField()),
                ("effect_name", models.CharField(max_length=16, verbose_name="效果")),
                (
                    "img",
                    models.ImageField(
                        blank="True", null=True, upload_to="img/", verbose_name="图鉴图片"
                    ),
                ),
                (
                    "img_detail",
                    models.ImageField(
                        blank="True", null=True, upload_to="img/", verbose_name="图鉴细节图片"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ListOfAllModel",
        ),
    ]
