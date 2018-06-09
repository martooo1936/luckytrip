import sqlite3

# define the connection

conn = sqlite3.connect('luckytrip.db')

# define the cursor
c = conn.cursor()


def get_destinations():
    # get all the data in the table
    c.execute('SELECT * FROM destinations')
    # assign all the data to a variable
    # iterate through the data => it is a tuple

    print("Our desinations are:")

    for row in c.fetchall():
        ticket = row[2]
        hotel = row[3]
        pocketm = row[4]
        totsum = ticket + hotel + pocketm
        print(row)
        #print(totsum)


def get_dest_byparam():

    # get destination by parameter
    bcd = input("enter budget\n")
    acd = int(bcd)
    c.execute("SELECT * FROM destinations ")

    for row in c.fetchall():
        ticket = row[2]
        hotel = row[3]
        pocketm = row[4]
        total = ticket + hotel + pocketm

        if total <= acd:
            print("your budget is enough for: " + row[1])


        else:
            print("your budget is not enough: " + row[1])


# get_destinations()
# get_dest_byparam()

while True:
    print("1. See our destinations")
    print("2 Check what you can afford")
    choice = input("Pick one option\n")
    if choice == "1":
        get_destinations()
    if choice == "2":
        get_dest_byparam()
    else:
        print("Chose a valid option ")

