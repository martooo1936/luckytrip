import sqlite3


# define the connection

conn = sqlite3.connect('luckytrip.db')

# define the cursor
c = conn.cursor()


# create a table in the db
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS destinations(country TEXT, city TEXT, ticket_price REAL, hotel_price REAL, pocketmoney REAL)')


# put data in the db
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


# insert_data()

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
