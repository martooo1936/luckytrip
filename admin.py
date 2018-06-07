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


# get all destinations
def get_excursions():
    c.execute("SELECT * FROM destinations")
    for row in c.fetchall():
        print(row)


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


#update_destination()

def update_country():
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]
    new_country = input("Which country you want to add\n")
    old_country = input("Which country you want to replce\n")
    c.execute("UPDATE  destinations SET country=(?) WHERE country=(?)",
              (new_country, old_country))
    conn.commit()
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]


def update_ticket_price():
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]
    new_price = input("What is the new price\n")
    city = input("Which destination you want to change\n")
    c.execute("UPDATE  destinations SET ticket_price=(?) WHERE city=(?)",
              (new_price, city))
    conn.commit()
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]


def update_hotel_price():
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]
    new_price = input("What is the new price of the stay\n")
    city = input("Which destination you want to change\n")
    c.execute("UPDATE  destinations SET hotel_price=(?) WHERE city=(?)",
              (new_price, city))
    conn.commit()
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]



def update_pocket_money():
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]
    new_money = input("What is approx pocket money required\n")
    city = input("Which destination you want to change\n")
    c.execute("UPDATE  destinations SET pocketmoney=(?) WHERE city=(?)",
              (new_money, city))
    conn.commit()
    c.execute("SELECT * FROM destinations")
    [print(row) for row in c.fetchall()]


def delete_excursion():
    c.execute("SELECT  * FROM  destinations")
    [print(row) for row in c.fetchall()]
    city_to_del = input("Which excursion you want to delete\n")
    c.execute("DELETE FROM destinations WHERE city=(?)",
              (city_to_del, ))
    conn.commit()
    c.execute("SELECT  * FROM destinations")
    [print(row) for row in c.fetchall()]


# update_country()
# admin menu



while True:
    print("0. See current excursions")
    print("1. Insert new excursion")
    print("2. Update Country")
    print("3. Update City")
    print("4. Update Traveling Costs")
    print("5. Update Hotel Expenses")
    print("6. Update Pocket money needed")
    print("7. Delete Excursion")
    print("8. Quit")
    choice = input("Pick one option\n")
    if choice == "0":
        get_excursions()
    if choice == "1":
        insert_data()
    if choice == "2":
        update_country()
    if choice == "3":
        update_destination()
    if choice == "4":
        update_ticket_price()
    if choice == "5":
        update_hotel_price()
    if choice == "6":
        update_pocket_money()
    if choice == "7":
        delete_excursion()
    if choice == "8":
        break
    else:
        print("choose a valid option")
