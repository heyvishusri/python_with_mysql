import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Vishu9931@@@",
            database="pythontest",
        )
        query = "create table if not exists user(userId int primary key auto_increment,userName varchar(200), phoneNumber varchar(15),email varchar(200), password varchar(20))"
        cur = self.con.cursor()
        cur.execute(query)
        # print("table created")

    # insert data
    def insert_user(self, userName, phoneNumber, email, password):
        query = "insert into user(username, phoneNumber, email, password) values('{}','{}','{}','{}')".format(
            userName, phoneNumber, email, password
        )
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user added")

    # fetch data
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId:", row[0])
            print("UserName:", row[1])
            print("PhoneNumber:", row[2])
            print("Email:", row[3])
            print("Password:", row[4])
            print("====================================")
            print()

    # fetch user by id
    def fetch_user_by_id(self, userId):
        query = "select * from user where userId={}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("🥳User found!")
            print()
            print("UserId:", row[0])
            print("UserName:", row[1])
            print("PhoneNumber:", row[2])
            print("Email:", row[3])
            print("Password:", row[4])
            print("====================================")
            print()

    # delete user by id
    def delete_user_by_id(self, userId):
        query = "delete from user where userId={}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user deleted successfully🥺")

    # update records
    def update_user_by_id(self, userId, newName, newEmail, newPhone, newPassword):
        query = "update user set userName='{}', phoneNumber='{}', email='{}', password='{}' where userId={}".format(
            newName, newPhone, newEmail, newPassword, userId
        )
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user updated successfully😎")
