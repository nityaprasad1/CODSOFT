import mysql.connector

mydb = mysql.connector.connect(user='root', password='root', host='localhost', database='hotel')
mycursor = mydb.cursor()

def registercust():
    name = input("Enter your name: ")
    addr = input("Enter your address: ")
    indate = input("Enter check-in date (YYYY-MM-DD): ")
    outdate = input("Enter check-out date (YYYY-MM-DD): ")
    sql = "INSERT INTO custdata (custname, addr, indate, outdate) VALUES (%s, %s, %s, %s)"
    val = (name, addr, indate, outdate)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Customer registered successfully!")

def roomtypeview():
    sql = "SELECT * FROM roomtype"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def roomrent():
    print("We have the following rooms for you:")
    print("1. Type A --> Rs 1000 per night")
    print("2. Type B --> Rs 2000 per night")
    print("3. Type C --> Rs 3000 per night")
    print("4. Type D --> Rs 4000 per night")

    choice = int(input("Enter your choice: "))
    nights = int(input("For how many nights did you stay: "))
    
    if choice == 1:
        rent = 1000 * nights
        room_type = "A"
    elif choice == 2:
        rent = 2000 * nights
        room_type = "B"
    elif choice == 3:
        rent = 3000 * nights
        room_type = "C"
    elif choice == 4:
        rent = 4000 * nights
        room_type = "D"
    else:
        print("Invalid choice.")
        return

    print(f"You have opted for room type {room_type}. Your total room rent is Rs {rent}.")

def restaurentmenuview():
    sql = "SELECT * FROM restaurant"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def orderitem():
    restaurentmenuview()
    
    menu = {
        1: ("Tea", 10),
        2: ("Coffee", 10),
        3: ("Colddrink", 20),
        4: ("Samosa", 10),
        5: ("Sandwich", 50),
        6: ("Dhokla", 30),
        7: ("Kachori", 10),
        8: ("Milk", 20),
        9: ("Noodles", 50),
        10: ("Pasta", 50),
    }

    choice = int(input("Enter the item number you want to order: "))
    if choice in menu:
        item, price = menu[choice]
        quantity = int(input(f"How many {item}s would you like to order? "))
        total = price * quantity
        print(f"Your total amount for {quantity} {item}(s) is Rs {total}.")
    else:
        print("Invalid choice. Please select an item from the menu.")

def laundarybill():
    global z
    print("Do you want to see the rates for laundry? Enter 1 for yes: ")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        sql = "SELECT * FROM laundry"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
    y = int(input("Enter the number of clothes: "))
    z = y * 10
    print("Your laundry bill is Rs", z)
    return z

def Menuset():
    print("Enter 1: To enter customer data")
    print("Enter 2: To view room type")
    print("Enter 3: For calculating room bill")
    print("Enter 4: For viewing restaurant menu")
    print("Enter 5: For restaurant bill")
    print("Enter 6: For laundry bill")
    print("Enter 7: For exit")
    try:
        userinput = int(input("Please select an above option: "))
    except ValueError:
        exit("\nHi, that's not a number.")
    
    if userinput == 1:
        registercust()
    elif userinput == 2:
        roomtypeview()
    elif userinput == 3:
        roomrent()
    elif userinput == 4:
        restaurentmenuview()
    elif userinput == 5:
        orderitem()
    elif userinput == 6:
        laundarybill()
    elif userinput == 7:
        print('Thanks for visiting')
        quit()
    else:
        print("Enter correct choice")

def runagain():
    runagn = input("\nWant to run again y/n: ")
    while runagn.lower() == 'y':
        Menuset()
        runagn = input("\nWant to run again y/n: ")

if __name__ == "__main__":
    Menuset()
    runagain()
