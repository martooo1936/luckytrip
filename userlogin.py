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


def create_user():
    username = input("Username ? : \n")
    firstName = input("First name ? :\n")
    lastName = input("Last name ? : \n")
    passWord =input("password ? : \n")
    c.execute("INSERT INTO users(username, first_name, last_name, password) VALUES (?, ?, ?, ?)",
              (username, firstName, lastName, passWord))

    # commit the changes
    conn.commit()
    print("user is successfully saved in the db")


def get_users():
    c.execute("SELECT * from users")
    for row in c.fetchall():
        print(row)


#create_user()
get_users()