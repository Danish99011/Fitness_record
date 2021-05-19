# HEALTH MANAGEMENT SYSTEM
print("\t\t\t\t\t ****** HEALTH MANAGEMENT SYSTEM ****** \n ")
print("We have three people here whose record will be maintained:")
print("1. Danish")
print("2. Vedaant")
print("3. Deepanshu")
n = int(input("Press 1-3 for selecting the respective client:"))
import datetime


def gettime():
    """This is used to add current time of registration of the data"""
    return datetime.datetime.now()


while True:
    if n == 1:
        print("What do you want to add in Danish's chart??")
        print("1. EXERCISE")
        print("2. FOOD")
        c = int(input())
        if c == 1:
            f = open("danish-exercise.txt", "a")
            print("Enter the name of exercise:")
            d = input()
            f.write(str([str(gettime())]) + " - " + d + "\n")
            print("Data is successfully added.")
            print(str([str(gettime())]) + " - " + d + "\n")
            f.close()
            print("Do you want to add something more??")
            print("Press ""Y"" for yes and ""N"" for no.")
            m = input()
            if m == "Y":
                continue
            elif m == "N":
                break
            else:
                print("You have entered something wrong.")
                break
        elif c == 2:
            f = open("danish-food.txt", "a")
            print("Enter the name of food:")
            d = input()
            f.write(str([str(gettime())]) + " - " + d + "\n")
            print("Data is successfully added.")
            print(str([str(gettime())]) + " - " + d + "\n")
            f.close()
            print("Do you want to add something more??")
            print("Press ""Y"" for yes and ""N"" for no.")
            m = input()
            if m == "Y":
                continue
            elif m == "N":
                break
            else:
                print("You have entered something wrong.")
                break
        else:
            print("You have entered something wrong.")
            break
    elif n == 2:
        print("What do you want to add in vedaant's chart??")
        print("1. Exercise")
        print("2. Food")
        c = int(input())
        if c == 1:
            f = open("vedaant-exercise.txt", "a")
            print("Enter the name of exercise:")
            d = input()
            f.write(str([str(gettime())]) + " - " + d + "\n")
            print("Data is successfully added.")
            print(str([str(gettime())]) + " - " + d + "\n")
            f.close()
            print("Do you want to add something more??")
            print("Press ""Y"" for yes and ""N"" for no.")
            m = input()
            if m == "Y":
                continue
            elif m == "N":
                break
            else:
                print("You have entered something wrong.")
                break
        elif c == 2:
            f = open("vedaant-food.txt", "a")
            print("Enter the name of food:")
            d = input()
            f.write(str([str(gettime())]) + " - " + d + "\n")
            print("Data is successfully entered.")
            print(str([str(gettime())]) + " - " + d + "\n")
            f.close()
            print("Do you want to add something more??")
            print("Press ""Y"" for yes and ""N"" for no.")
            m = input()
            if m == "Y":
                continue
            elif m == "N":
                break
            else:
                print("You have entered something wrong.")
        else:
            print("You have entered something wrong.")
            break
    elif n == 3:
        print("What do you want to add in Deepanshu's chart??")
        print("1. EXERCISE")
        print("2. FOOD")
        c = int(input())
        if c == 1:
            f = open("deepanshu-exercise.txt", "a")
            print("Enter the name of exercise:")
            d = input()
            f.write(str([str(gettime())]) + " - " + d + "\n")
            print("Data is successfully added.")
            print(str([str(gettime())]) + " - " + d + "\n")
            f.close()
            print("Do you want to add something more??")
            print("Press ""Y"" for yes and ""N"" for no.")
            m = input()
            if m == "Y":
                continue
            elif m == "N":
                break
            else:
                print("You have entered something wrong.")
                break
        elif c == 2:
            f = open("deepanshu-food.txt", "a")
            print("Enter the name of food:")
            d = input()
            f.write(str([str(gettime())]) + " - " + d + "\n")
            print("Data is successfully added.")
            print(str([str(gettime())]) + " - " + d + "\n")
            f.close()
            print("Do you want to add something more??")
            print("Press ""Y"" for yes and ""N"" for no.")
            m = input()
            if m == "Y":
                continue
            elif m == "N":
                break
            else:
                print("You have entered something wrong.")
                break
        else:
            print("You have entered something wrong.")
            break

print()
print()
print("\t\t\t\t\t ****** THANK YOU ******")
