#  I delete all the quotation marks in input files to run the grader program correctly. 
user_dict = {}
logIn = False
def read_file():
    my_file = open("users.txt", encoding = "utf-8")
    for line in my_file:
        name, password, friend = line.split(";")
        user_dict[name] = [password, friend[:-1].split(",")]
    my_file.close()
def log_in(username,password):
    if username in user_dict and password == user_dict[username][0]:
        return True
    return False 
def check_username():
    username = input("Please enter username:\n")
    if username not in user_dict and username.isalnum():
        return username
    return False
def check_password():
    password = input("Please enter password:\n")
    if len(password) < 4 or len(password) > 8:
        return False
    letter = False
    number = False
    for i in password:
        if i.isalpha():
            letter = True
        elif i.isdigit():
            number = True
    if letter and number:
        return password
    return False
def create_user():
    username = check_username()
    if not username:
        print("Username not valid\n")
        return False
    password = check_password()
    if not password:    
        print("Password not valid\n")
        return False
    user_dict[username] = [password, []]
def add_friend(username):
    friend_name = input("Please enter the name of your new friend:\n")
    if friend_name not in user_dict:
        print("Friend not found\n")
    else:
        (user_dict[username][1]).append(friend_name)
def show_friend(username):
    friends_list = user_dict[username][1]
    friends = ""
    for friend in friends_list:
        friends = friends + friend +","
    print(friends[:-1])
def save_users():
    users = ""
    for k,v in user_dict.items():
        friends_list = v[1]
        friends = ""
        for friend in friends_list:
            friends = friends + friend +","
        users = users + k + ";" + str(v[0]) + ";" + friends[:-1] + "\n"
    the_file = open("test.txt", "w", encoding = "utf-8")
    the_file.write(users)
    the_file.close()
read_file()
while True:
    menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n"
    print(menu_text, end = "")
    option = input("")
    if option == "1":
        username = input("Please enter username:\n")
        password = input("Please enter password:\n")
        if log_in(username,password):
            print("Logged in\n")
            logIn = True
        else:
            print("Wrong password or username\n")
    elif option == "2":
        create_user()
    elif option == "3":
        if not logIn:
            print("You need to log in first\n")
        else:
            add_friend(username)
    elif option == "4":
        if not logIn:
            print("You need to log in first\n")
        else:
            show_friend(username)
    elif option == "5":
        save_users()
        break
    else:
        print("Invalid option\n")