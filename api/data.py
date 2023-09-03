import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zeldaRecipe.settings')
django.setup()
from api.models import *

from django.utils import timezone
import pymysql
# 获取数据库连接，创建游标
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='zelda_demo',
                       charset='utf8mb4'
                       )
cursor = conn.cursor()


def listOfEffect():
    sql = "INSERT INTO api_listofeffect (effect_id, effect_name) VALUES (%s, %s)"
    effectDict = [
        "攻击提升",
        "防御提升",
        "速度提升",
        "防热",
        "防寒",
        "耐火",
        "防雷",
        "潜行",
        "生命恢复",
        "耐力恢复"
    ]
    for i in range(len(effectDict)):
        cursor.execute(sql, (i+1, effectDict[i]))
    print("finished")
    conn.commit()


def listOfAllFruit():
    sql = "INSERT INTO api_listofall (id, class_id, class_name, item_name, item_name_cn, info, effect_id) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    foodDict = [
        ['Apple', '苹果', 'A', 10],
        ['GoldenApple', '金苹果', 'P', 11],
        ['PalmFruit', '椰子', 'G', 10],
        ['WildBerry', '草莓', 'B', 10],
        ['HylianTomato', '海拉鲁番茄', 'M', 10],
        ['ChilledMelon', '冰冷蜜瓜', 'F', 4],
        ['WarmFruit', '暖暖草果', 'I', 5],
        ['VoltFruit', '酥麻水果', 'C', 7],
        ['SpeedyLotus', '速速莲蓬', 'E', 3],
        ['MightyBananas', '大剑香蕉', 'H', 1],
        ['FireFruit', '火焰果', 'FireFruit', 1],
        ['IceFruit', '冷气果', 'IceFruit', 1],
        ['WaterFruit', '水之果', 'WaterFruit', 3],
        ['ElectricalFruit', '电流果', 'ElectricalFruit', 1],
        ['LightFruit', '闪耀果', 'LightFruit', 12],
    ]
    for i in range(len(foodDict)):

        cursor.execute(sql, (i+1, '1', 'fruit',
                             foodDict[i][0], foodDict[i][1], foodDict[i][2], foodDict[i][3]))
    print("finished")
    conn.commit()


def listOfClass():
    # 执行数据库crud操作
    # obj_list = [
    #     models.ListofClass(id=1, class_id=1),
    #     models.ListOfClass(id=2, class_id=1),
    #     models.ListOfClass(id=3, class_id=1)
    # ]
    # models.ListOfClass.objects.bulk_create(obj_list, batch_size=3)

    sql = "INSERT INTO api_listofclass (id, class_id) VALUES (%s, %s)"
    cursor.execute(sql, ('1', '1'))
    print("finished")
    conn.commit()


def listOfAllFish():
    sql = "INSERT INTO api_listofall (id, class_id, class_name, item_name, item_name_cn, info, effect_id) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    foodDict = [
        ['HylianFlatfish', '海拉鲁鲈鱼', 'A', 10],
        ['LatesFlatfish', '生命鲈鱼', 'B', 10],
        ['EnergyFlatfish', '精力鲈鱼', 'L', 9],
        ['LatesSalmon', '生命鲑鱼', 'I', 10],
        ['ChilledTrouts', '冰冷鳟鱼', 'C', 4],
        ['WarmTrouts', '暖暖鳟鱼', 'J', 5],
        ['VoltTrouts', '酥麻鳟鱼', 'D', 7],
        ['SilentTrouts', '潜行鳟鱼', 'X', 8],
        ['MightyCarps', '大剑鲤鱼', 'E', 1],
        ['ArmorCarps', '铠甲鲤鱼', 'H', 2],
        ['TricolorCarps', '三色鲤鱼', 'Z', 10],
        ['Diplopoda ', '远昔骨舌鱼', 'AA', 13],
        ['BrightHornfish', '光亮霍拉鱼', 'AC', 14],
        ['MightySnapper', '大剑鲷鱼', 'F', 1],
        ['ArmorSnapper', '铠甲鲷鱼', 'G', 2],
    ]
    for i in range(len(foodDict)):

        cursor.execute(sql, (i+16, '2', 'fish',
                             foodDict[i][0], foodDict[i][1], foodDict[i][2], foodDict[i][3]))
    print("finished")
    conn.commit()


def listOfAllRecipe():
    sql = "INSERT INTO api_recipe (dish_id, dish_name, name_cn, ingreOne_id, ingreTwo_id, ingreThree_id, ingreFour_id) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    foodDict = [
        ['ToastApple', '烤苹果', 1, 0, 0, 0],
        ['HotSpicyFriedFish', '香辣煎鱼', 7, 16, 0, 0]

    ]
    for i in range(len(foodDict)):
        cursor.execute(sql, (i+1,
                             foodDict[i][0], foodDict[i][1], foodDict[i][2],
                             foodDict[i][3], foodDict[i][4], foodDict[i][5],

                             )
        )
    print("finished")
    conn.commit()


if __name__ =='__main__':
    listOfAllRecipe()