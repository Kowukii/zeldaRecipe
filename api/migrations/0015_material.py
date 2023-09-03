# Generated by Django 4.2.3 on 2023-08-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_alter_recipe_dish_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Material",
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
                ("RowId", models.CharField(max_length=32, verbose_name="系统名称")),
                ("cn_name", models.CharField(max_length=32, verbose_name="中文名称")),
                ("DyeColor", models.CharField(max_length=8, verbose_name="染色")),
                ("IsUsable", models.BooleanField()),
                ("BuyingPrice", models.IntegerField()),
                ("PouchGetType", models.CharField(max_length=8)),
                ("PouchSortKey", models.IntegerField()),
                ("PouchUseType", models.CharField(max_length=8, verbose_name="用途")),
                ("SellingPrice", models.IntegerField()),
                ("PouchCategory", models.CharField(max_length=8, verbose_name="种类")),
                ("BundleActorNum", models.IntegerField()),
                ("CureEffectType", models.CharField(max_length=8, verbose_name="功效")),
                ("PouchStockable", models.BooleanField()),
                ("CureEffectLevel", models.IntegerField()),
                (
                    "PouchSpecialDeal",
                    models.CharField(max_length=16, verbose_name="特殊作用"),
                ),
                ("CureEffectiveTime", models.IntegerField()),
                ("info", models.CharField(max_length=128, verbose_name="简介")),
            ],
        ),
    ]
