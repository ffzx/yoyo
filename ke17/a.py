"""
连接mysql
49.235.92.12  3309
root 123456
apps
"""
import pymysql

db = pymysql.connect(host="49.235.92.12",
                     user="root",
                     password="123456",
                     database="apps",
                     port=3309,
                     cursorclass=pymysql.cursors.DictCursor
                     )
# 创建游标
cur = db.cursor()
sql = 'SELECT * from auth_user WHERE username="test";'
cur.execute(sql)
result = cur.fetchall()  # 得到查询结果
print(result)

# 新增 修改 删除
sql2 = """
UPDATE `apps`.`auth_user` SET `id`='5', `password`='pbkdf2_sha256$100000$fda6949Ergzt$Rg0Y3V+1ImCybc8kFX7PZ2a+P5rZOFLhFP3GX9xum/o=', 
`last_login`=NULL, `is_superuser`='0', `username`='test2', `first_name`='', `last_name`='', `email`='333@qq.com', `is_staff`='0', 
`is_active`='1', `date_joined`='2021-05-04 23:13:47.343870' WHERE (`id`='5');
"""
cur.execute(sql2)
# 提交
db.commit()

# 关闭游标 关闭数据库连接
cur.close()
db.close()
