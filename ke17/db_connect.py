import pymysql

dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309}


class DBConnect():

    def __init__(self, dbinfo: dict, database='db'):
        self.dbinfo = dbinfo
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **dbinfo)
        self.cursor = self.db.cursor()

    def select(self, sql):
        """查询结果 [{}]"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        """新增，删除，修改"""
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as msg:
            print(f"执行sql: {sql}, 出现异常:{msg}")
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    db = DBConnect(dbinfo, database="apps")
    sql = 'SELECT * from auth_user WHERE username="test";'
    res = db.select(sql)
    print(res)