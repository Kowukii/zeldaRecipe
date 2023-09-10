from django.db import models

# Create your models here.

class UserModel(models.Model):
    app_label = 'user'
    material_name = models.CharField(max_length=30, unique=True)
    # 食材名称
    material_region = models.CharField(max_length=30)
    # 食材出现区域
    material_feature = models.CharField(max_length=30)
    # 食材特性
    material_info = models.CharField(max_length=128)
    # 食材介绍
    food_name = models.CharField(max_length=30)
    # 菜肴名称
    food_recipe = models.CharField(max_length=30)
    # 菜肴组成S
    food_feature = models.CharField(max_length=30)
    # 菜肴特性

    def __str__(self):
        return f'{self.material_name}'

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(verbose_name="名称", max_length=16, default='')
    item_name_cn = models.CharField(verbose_name="cn名称", max_length=8, default='')
    class_id = models.IntegerField()
    class_name = models.CharField(verbose_name="类名称", max_length=16, default='')
    info = models.CharField(verbose_name="简介", max_length=32, default='')
    effect_id = models.IntegerField(default=10)
    img_path = models.CharField(verbose_name="img路径", max_length=64, default=' ')
    imgDetail_path = models.CharField(verbose_name="Detail路径", max_length=64, default=' ')


class ClassOfIngredients(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(verbose_name="类名称", max_length=16)
    name_cn = models.CharField(verbose_name="cn类名称", max_length=16)





class ListOfEffect(models.Model):
    effect_id = models.IntegerField(primary_key=True, default=0, auto_created=True)
    effect_name = models.CharField(verbose_name="类名称", max_length=16)


class Recipe(models.Model):
    dish_id = models.IntegerField(default=0,primary_key=True)
    name_cn = models.CharField(verbose_name="cn名称", max_length=16)
    name_en = models.CharField(verbose_name="en名称", max_length=64, default='')
    dish_info = models.CharField(verbose_name="简介", max_length=1024, null=True)
    dish_info_en = models.CharField(verbose_name="en简介", max_length=1024, null=True)
    para = models.CharField(verbose_name="加成", max_length=32, default='')
    ingre1 = models.CharField(verbose_name="原料1", max_length=32, null=True)
    ingre2 = models.CharField(verbose_name="原料2", max_length=32, null=True)
    ingre3 = models.CharField(verbose_name="原料3", max_length=32, null=True)
    ingre4 = models.CharField(verbose_name="原料4", max_length=32, null=True)
    img_path = models.CharField(verbose_name="img路径", max_length=64, default='')


class Material(models.Model):
    RowId = models.CharField(verbose_name="系统名称", max_length=32)
    cn_name = models.CharField(verbose_name="中文名称", max_length=32)
    DyeColor = models.CharField(verbose_name="染色", max_length=32)
    IsUsable = models.BooleanField()
    BuyingPrice = models.IntegerField()
    PouchGetType = models.CharField(max_length=16)
    PouchSortKey = models.IntegerField()
    PouchUseType = models.CharField(verbose_name="用途", max_length=32)
    SellingPrice = models.IntegerField()
    PouchCategory = models.CharField(verbose_name="种类", max_length=32)
    BundleActorNum = models.IntegerField()
    CureEffectType = models.CharField(verbose_name="功效", max_length=32)
    PouchStockable = models.BooleanField()
    CureEffectLevel = models.IntegerField()
    PouchSpecialDeal = models.CharField(verbose_name="特殊作用", max_length=32)
    CureEffectiveTime = models.IntegerField()
    info = models.CharField(verbose_name="简介", max_length=256)
    img_path = models.CharField(verbose_name="img路径", max_length=64, default=' ')
    HitPointRecover = models.IntegerField(default=0)
    class_name = models.CharField(verbose_name="类名称", max_length=16, default='')

