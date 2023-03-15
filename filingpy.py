import msvcrt
print("My FIling Program")


def additem():
    choice = '1'
    myFile = open("D:\\data.txt", 'w')
    while choice == '1':
        serialID = input("Enter serial ID: ")
        brandName = input("Enter your brand name: ")
        itemPrice = input("Enter product price: ")

        myFile.write(serialID + "\t" + brandName + "\t" + itemPrice +"\n")
        print("Enter 1 to add more items")
        choice = msvcrt.getch().decode('ASCII')
    
def delitem():
    delFile = open("D:\\data.txt","r+")
    #print(delFile.read())
    extracted = [0,0]
    toDelete = input("Enter serialID to be deleted: ")
    while extracted[0] != toDelete:
        extracted = str(delFile.readline()).split("\t")
        print(extracted)

def menu():
    key = '0'
    while (key != '1') and (key != '2'):
        print("This is Main Menu:")
        print("1. Add Item")
        print("2. Delete Item")
        key = msvcrt.getch().decode('ASCII')
        if key == '1':
            additem()
        elif key == '2':
            delitem()
        else:
            print("Bhai jaan input sahi dalo")


menu()
