import msvcrt
import os


def listitem():
    os.system("CLS")
    myFile = open("data.txt", "r")
    print("Serial ID" +"\t"+"Brand Name"+"\t"+"Price($)")
    for z in myFile:
        a,b,c = z.strip("\n").split("\t")
        print(a + "\t\t" + b + "\t\t"+ c)
    msvcrt.getch()

    myFile.close()


def additem():
    choice = '1'
    myFile = open("data.txt", 'w')
    while choice == '1':
        serialID = input("Enter serial ID: ")
        brandName = input("Enter your brand name: ")
        itemPrice = input("Enter product price: ")

        myFile.write(serialID + "\t" + brandName + "\t" + itemPrice +"\n")
        print("Enter 1 to continue adding itmes")
        choice = msvcrt.getch().decode('ASCII')

    myFile.close()
    
def delitem():
    delFile = open("data.txt","r+")
    temp = open("temp.txt","w")
    extracted = delFile.readlines()
    listitem()
    toDelete = input("Enter serialID to be deleted: ")
    for line in extracted:
        field = line.split("\t")

        if field[0] == toDelete:
            print("Record found!")
            print(line)
            print("Press any key to delete")
            msvcrt.getch()
        else:
            temp.write(line)

    delFile.close()
    temp.close()

    os.remove("data.txt")
    os.rename("temp.txt","data.txt")

def appenditem():
    choice = '1'
    appendFile = open('data.txt','a')
    while choice == '1':
        serialID = input("Enter serial ID: ")
        brandName = input("Enter your brand name: ")
        itemPrice = input("Enter product price: ")

        appendFile.write(serialID + "\t" + brandName + "\t" + itemPrice +"\n")
        print("Enter 1 one to continue adding items")
        choice = msvcrt.getch().decode('ASCII')

def modifyitem():
    modFile = open("data.txt","r+")
    temp = open("temp.txt","w")
    extracted = modFile.readlines()
    listitem()
    toModify = input("Enter serialID to be modified: ")
    for line in extracted:
        field = line.split("\t")

        if field[0] == toModify:
            print("Record found!")
            print(line)
            serialID = input("Enter new serial ID: ")
            brandName = input("Enter your brand name: ")
            itemPrice = input("Enter product price: ")
            temp.write(serialID + "\t" + brandName + "\t" + itemPrice +"\n")
            char = msvcrt.getch()
        else:
            temp.write(line)

    modFile.close()
    temp.close()

    os.remove("data.txt")
    os.rename("temp.txt","data.txt")


def sort():
    oldFile = open('data.txt','r')
    newFile = open('temp.txt','w')

    isSwap = True
    myArray = []

    fileLen = len(oldFile.readlines())
    oldFile.seek(0)

    
    for i in range(fileLen):
        line = oldFile.readline().split("\t")
        myArray.append(line)

    while isSwap == True:
        isSwap = False
        for c in range(fileLen-1):
            if (int(myArray[c][0]) > int(myArray[c+1][0])):
                temp = myArray[c] 
                myArray[c] = myArray[c+1]
                myArray[c+1] = temp
                isSwap = True
            

    for x in myArray:
        newFile.write(x[0] + "\t" + x[1] + "\t" + x[2])

    oldFile.close()
    newFile.close()

    os.remove('data.txt')
    os.rename('temp.txt','data.txt')

    os.system("CLS")

    print("File sorted successfully!")

    msvcrt.getch()



def menu():
    key = '0'
    while (key != '9'):
        os.system("CLS")
        print("Main Menu")
        print("-"*9)
        print("1. New File")
        print("2. Delete Item")
        print("3. List Items")
        print("4. Append Item")
        print("5. Modify Item")
        print("6. Sort File")
        print("\n9. Exit")
        key = msvcrt.getch().decode('ASCII')
        if key == '1':
            additem()
        elif key == '2':
            delitem()
        elif key == '3':
            listitem()
        elif key == '4':
            appenditem()
        elif key == '5':
            modifyitem()
        elif key == '6':
            sort()
        elif key == '9':
            break
        else:
            print("Invalid input!")


menu()
