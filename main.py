from dbhelper import DBHelper


def main():
    Db = DBHelper()
    while True:
        print("💻WELCOME TO USER MANAGEMENT SYSTEM💻")
        print("====================================")
        print()
        print("PRESS 1 TO INSERT USER")
        print("PRESS 2 TO FETCH ALL USERS")
        print("PRESS 3 TO FETCH USER BY ID")
        print("PRESS 4 TO DELETE USER BY ID")
        print("PRESS 5 TO UPDATE USER BY ID")
        print("PRESS 6 TO EXIT")
        print()
        try:
            choice = int(input("ENTER YOUR CHOICE: "))
            print()
            if choice == 1:
                # insert user
                inter_name = input("Enter User Name: ")
                inter_phone = input("Enter Phone Number: ")
                inter_email = input("Enter Email: ")
                inter_password = input("Enter Password: ")
                Db.insert_user(inter_name, inter_phone, inter_email, inter_password)
                pass
            elif choice == 2:
                # fetch all users
                Db.fetch_all()
                pass
            elif choice == 3:
                # fetch user by id
                inter_id = int(input("Enter User ID to fetch: "))
                Db.fetch_user_by_id(inter_id)
                pass
            elif choice == 4:
                # delete user by id
                inter_id = int(input("Enter User ID to delete: "))
                Db.delete_user_by_id(inter_id)
                print()
                pass
            elif choice == 5:
                # update user by id
                inter_id = int(input("Enter User ID to update: "))
                inter_name = input("Enter new User Name: ")
                inter_email = input("Enter new Email: ")
                inter_phone = input("Enter new Phone Number: ")
                inter_password = input("Enter new Password: ")
                Db.update_user_by_id(
                    inter_id, inter_name, inter_email, inter_phone, inter_password
                )
                pass
            elif choice == 6:
                print("Exiting...👋")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print("Error:", e)
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
