import sqlite3

connUsers = sqlite3.connect('luckyusers.db')
c2 = connUsers.cursor()

c2.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY , 
    username VARCHAR(20) NOT NULL , 
    first_name VARCHAR(20)NOT NULL , 
    last_name VARCHAR(20) NOT NULL , 
    password VARCHAR(20) NOT NULL 
    
  )  
    ''')


def encrypt_pass(password):
    encrypttedText = ""
    for letter in password:
        cipher = ord(letter) + 10
        encrypttedText += chr(cipher)
    return encrypttedText


def decrypt_pass(password):
    decrypted = ""
    for letter in password:
        cipher = ord(letter) - 10
        decrypted += chr(cipher)
    return decrypted






def create_user():
    username = input("Username ? : \n")
    firstName = input("First name ? :\n")
    lastName = input("Last name ? : \n")
    passWord =input("password ? : \n")
    c2.execute("INSERT INTO users(username, first_name, last_name, password) VALUES (?, ?, ?, ?)",
               (username, firstName, lastName, encrypt_pass(passWord)))

    # commit the changes
    connUsers.commit()

    print("user is successfully saved in the db")
    c2.execute("SELECT * FROM users")
    for row in c2.fetchall():
        print(row)



def get_users():
    c2.execute("SELECT username, first_name, last_name from users")
    for row in c2.fetchall():
        print(row)


def delete_user():

    c2.execute("SELECT username FROM users")
    for row in c2.fetchall():
        print(row)
    user_to_del = input("which user you want to remove\n")

    c2.execute("DELETE FROM users WHERE username=(?)",
               (user_to_del, ))
    connUsers.commit()
    # show updated list
    c2.execute("SELECT * FROM users")
    for row in c2.fetchall():
        print(row)


def login():
    while True:
        username = input("enter username\n")
        password = input("enter pass:\n")
        pass2 = encrypt_pass(password)

        find_user = c2.execute("SELECT * FROM users WHERE username = (?) AND password = (?)",
                               (username, pass2))
        result = c2.fetchall()

        if result:
            for i in result:
                print("Welcome " + i[2])
        else:
            print("User login is invalid to proceed enter valid credentials")



#delete_user()
#create_user()
#get_users()
#login()


while True:
    print("1. Create new user")
    print("2. Delete existing user")
    print("3. See all existing users")
    print("4. Test login functionality")
    print("5. QUIT")
    choice = input("Select an option:\n")
    if choice == "1":
        create_user()
    if choice == "2":
        delete_user()
    if choice == "3":
        get_users()
    if choice == "4":
        login()
    if choice == "5":
        break
    else:
        print("choose a valid option")
