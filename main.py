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


# main code
helper = DBHelper()
# insert some users
# helper.insert_user("Vishwash", "1234567890", "vkumar080@rku.ac.in", "Vishu9931@@@")
# helper.insert_user("Alok", "1234567820", "akumar111@rku.ac.in", "Vishu9931@@@")
# helper.insert_user("Ritesh", "1234567820", "akumar111@rku.ac.in", "Vishu9931@@@")
# fetch all users
# helper.fetch_all()
# fetch user by id
# helper.fetch_user_by_id(3)
# delete user by id
# helper.delete_user_by_id(4)
