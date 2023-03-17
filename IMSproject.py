import msvcrt
import os
print("My FIling Program")


def additem():
    choice = '1'
    myFile = open("data.txt", 'w')
    while choice == '1':
        serialID = input("Enter serial ID: ")
        brandName = input("Enter your brand name: ")
        itemPrice = input("Enter product price: ")

        myFile.write(serialID + "\t" + brandName + "\t" + itemPrice +"\n")
        print("Enter 1 to add more items")
        choice = msvcrt.getch().decode('ASCII')
    
def delitem():
    delFile = open("data.txt","r+")
    temp = open("temp.txt","w")
    extracted = delFile.readlines()
    print(extracted)
    delFile.seek(0)
    toDelete = input("Enter serialID to be deleted: ")
    for line in extracted:
        field = line.split("\t")

        if field[0] == toDelete:
            print("Record found!")
            print(line)
            print("Press any key to delete")
            char = msvcrt.getch()
        else:
            temp.write(line)

    delFile.close()
    temp.close()

    os.remove("data.txt")
    os.rename("temp.txt","data.txt")


def menu():
    key = '0'
    while (key != '9'):
        print("This is Main Menu:")
        print("1. Add Item")
        print("2. Delete Item")
        print("9. Exit")
        key = msvcrt.getch().decode('ASCII')
        if key == '1':
            additem()
        elif key == '2':
            delitem()
        elif key == '9':
            break
        else:
            print("Invalid input!")


menu()
