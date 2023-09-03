# Generated by Django 4.2.3 on 2023-09-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0026_class_delete_listofclass"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ListOfAll",
        ),
        migrations.RemoveField(
            model_name="class",
            name="name",
        ),
        migrations.AddField(
            model_name="class",
            name="effect_id",
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name="class",
            name="imgDetail_path",
            field=models.CharField(default=" ", max_length=64, verbose_name="Detail路径"),
        ),
        migrations.AddField(
            model_name="class",
            name="img_path",
            field=models.CharField(default=" ", max_length=64, verbose_name="img路径"),
        ),
        migrations.AddField(
            model_name="class",
            name="info",
            field=models.CharField(default="", max_length=32, verbose_name="简介"),
        ),
        migrations.AddField(
            model_name="class",
            name="item_name",
            field=models.CharField(default="", max_length=16, verbose_name="名称"),
        ),
        migrations.AddField(
            model_name="class",
            name="item_name_cn",
            field=models.CharField(default="", max_length=8, verbose_name="cn名称"),
        ),
        migrations.AlterField(
            model_name="class",
            name="class_name",
            field=models.CharField(default="", max_length=16, verbose_name="类名称"),
        ),
    ]