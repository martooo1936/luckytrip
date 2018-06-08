import sqlite3

conn = sqlite3.connect('luckyusers.db')
c = conn.cursor()

c.execute('''
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
    c.execute("INSERT INTO users(username, first_name, last_name, password) VALUES (?, ?, ?, ?)",
              (username, firstName, lastName, encrypt_pass(passWord)))

    # commit the changes
    conn.commit()
    print("user is successfully saved in the db")


def get_users():
    c.execute("SELECT username, first_name, last_name from users")
    for row in c.fetchall():
        print(row)


def login():
    while True:
        username = input("enter username\n")
        password = input("enter pass:\n")
        pass2 = encrypt_pass(password)

        find_user = c.execute("SELECT * FROM users WHERE username = (?) AND password = (?)",
                              (username, pass2))
        result = c.fetchall()

        if result:
            for i in result:
                print("Welcome " + i[2])
        else:
            print("User login is invalid to proceed enter valid credentials")



#create_user()
#get_users()
login()

