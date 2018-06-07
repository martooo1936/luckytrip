import sqlite3


# define the connection

conn = sqlite3.connect('luckytrip.db')

# define the cursor
c = conn.cursor()


# create a table in the db
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS destinations(country TEXT, city TEXT, ticket_price REAL, hotel_price REAL, pocketmoney REAL)')


# put data in the db with sql statement
def data_entry():
    c.execute("INSERT INTO destinations VALUES ('Italy', 'Rome', 2244, 7711, 897)")
    conn.commit()
    # close the cursor
    c.close()
    # cloe the connenction
    conn.close()


# insert data from input
def insert_data():
    country = input("Enter a name of the country\n")
    city = input("Enter city name\n")
    ticket_price = input("aprox ticket price\n")
    hotel_price = input("aprox hotel price\n")
    pocketmoney = input("aprox pocket money needed\n")
    print("The country is saved in the db")
    c.execute("INSERT INTO destinations(country, city, ticket_price, hotel_price, pocketmoney) VALUES (?,?,?,?,?)",
              (country, city, ticket_price, hotel_price, pocketmoney))
    conn.commit()
    c.close()
    conn.close()


def update_destination():
    c.execute("SELECT  * FROM destinations")
    # one line for loop to print out every row for every row in c.fetchall()

    [print(row) for row in c.fetchall()]
    val_to_change = input("Which is the new city\n")
    new_value = input("Which one you want to replace\n")
    c.execute("UPDATE destinations SET city = (?) WHERE city = (?)",
              (val_to_change, new_value))
    conn.commit()
    # see the updated list
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]


update_destination()

# admin menu
"""

while True:
    print("1. Insert new excursion")
    print("2. Quit")
    choice = input("Pick one option\n")
    if choice == "1":
        insert_data()
    if choice == "2":
        break
    else:
        print("choose a valid option")
"""