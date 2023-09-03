import pymysql
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    passwd='root',
    charset='utf8',
    db='zelda_demo'

)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 收发指令的handler

# cursor.execute("insert into classofingredients(class_name, name_cn) values('medicine', '药材') ")
# conn.commit()
# 不要用字符串格式化做SQL拼接，安全隐患SQL注入
# 在增删改时要有commit
cursor.execute("select * from classofingredients")
data_list = cursor.fetchall()
for row_dict in data_list:
    print(row_dict)

cursor.close()
conn.close()
