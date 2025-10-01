from dbhelper import DBHelper


def main():
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
            if choice == 1:
                # insert user
                pass
            elif choice == 2:
                # fetch all users
                pass
            elif choice == 3:
                # fetch user by id
                pass
            elif choice == 4:
                # delete user by id
                pass
            elif choice == 5:
                # update user by id
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
# update user by id
helper.update_user_by_id(5, "Vishal")
