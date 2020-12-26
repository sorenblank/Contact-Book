import sqlite3
base = sqlite3.connect("contact_book.db")
cur = base.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Contact (Name TEXT, Number TEXT)")

while True:
    print("Choose An Option- ")
    print("1/ Add Contact")
    print("2/ Remove Contact")
    print("3/ Edit Contact")
    print("4/ See all contacts")
    print("5/ Search contact")
    print("6/ Exit")
    ask = int(input("Input: "))

    #option_1
    if ask == 1:
        print()
        while True:
            que_1_of_1 = input("Name: ").capitalize()
            que_2_of_1 = input("Number: ")
            cur.execute("INSERT INTO Contact (Name, Number) VALUES(?, ?)", (que_1_of_1, que_2_of_1))
            base.commit()
            cur.execute("SELECT*FROM Contact")
            all = cur.fetchall()
            if (que_1_of_1, que_2_of_1) in all:
                print()
                print("Operation Successfull")
                print()
            else:
                print()
                print("Operation Unsuccessfull")
                print()
            print("Do you want to add another contact? y/n")
            que_3_of_1 = input()
            if que_3_of_1 == "n":
                print()
                break

    #option_2
    elif ask == 2:
        cur.execute("SELECT*FROM Contact")
        all = cur.fetchall()
        if len(all) > 0:
            while True:
                print()
                cur.execute("SELECT*FROM Contact")
                all = cur.fetchall()
                ii = 1
                for i in all:
                    print(ii, i[0])
                    ii = ii + 1
                que1_of_2 = int(input("Which contact you want to remove: "))
                element = all[que1_of_2 - 1][1]
                cur.execute("DELETE FROM Contact WHERE Number = ?", (element,))
                base.commit()
                if element not in all:
                    print()
                    print("Operation Successful")
                else:
                    print()
                    print("Operation Unsccessful")
                print()
                cur.execute("SELECT*FROM Contact")
                all = cur.fetchall()
                if len(all) > 0:
                    print("Do you want to remove more? y/n")
                    que2_of_2 = input()
                    if que2_of_2 == "n":
                        break
                else:
                    break
        else:
            print()
            print("List Empty")
            print()

    #option_3
    elif ask == 3:
        print()
        cur.execute("SELECT*FROM Contact ORDER BY NAME ASC")
        all = cur.fetchall()
        if len(all) > 0:
            ii = 1
            for i in all:
                print(ii, i[0])
                ii = ii + 1
        else:
            print("The list is empty")
        print()
        que_1_of_3 = int(input("Which contact you want to edit: "))
        print()

        name = all[que_1_of_3-1][0]
        number = all[que_1_of_3-1][1]

        print("Name:", name)
        print("Number:", number)
        print()

        new_num = (input("New Number: "))
        cur.execute("UPDATE Contact SET Number = ? WHERE Number = ?", (new_num, number))
        base.commit()

        cur.execute("SELECT*FROM Contact ORDER BY NAME ASC")
        all = cur.fetchall()
        print()
        if (name, new_num) in all:
            print("Operation Successful")
        else:
            print("Operation Unsuccessful")

    #option_4
    elif ask == 4:
        print()
        cur.execute("SELECT*FROM Contact ORDER BY NAME ASC")
        all = cur.fetchall()
        if len(all) > 0:
            ii = 1
            for i in all:
                print(ii, i[0], '-', i[1])
                ii = ii + 1
            print(all)
        else:
            print("The list is empty")
        print()

    #option 5
    elif ask == 5:
        search=input("Search: ")
        print()
        cur.execute("SELECT*FROM Contact WHERE NAME LIKE ? ORDER BY NAME",(search+"%",))
        all = cur.fetchall()
        if len(all) > 0:
            ii = 1
            for i in all:
                print(ii, i[0], '-', i[1])
                ii = ii + 1
        else:
            print("The list is empty")
        print()

    #option_6
    elif ask == 6:
        break

    else:
        print("please try again")