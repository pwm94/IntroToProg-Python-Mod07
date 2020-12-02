# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with exceptions and pickling
# ChangeLog (Who,When,What):
# <Paul Mitchell>,<12/01/2020>, created code to complete assignment 7
# ---------------------------------------------------------------------------- #

OptionVar = str(0)
StoredData = []
while (True):
    print("\nDatabase of Adoptable Dogs & Their Ages:")
    print("1) Add Dogs to List")
    print("2) Display Current Dogs")
    print("3) Unpickle & Reload List of Dogs from File")
    print("4) Pickle and Save to File")
    print("5) Exit Program")
    UserInput = str((input("Which option would you like to perform:z [1] to [5]? ")))
    try:
        import math
        x = int(5)
        y = int(UserInput)
        z = x - abs(y)
        test = math.sqrt(z)
        testforzero = 1 / y
        OptionVar = UserInput
        if (OptionVar == str(1)):
            print("\nEnter the Name and Age for the new dog below")
            DogName = str(input("Enter a Name: "))
            DogAge = str(input("Enter an Age: "))
            ListRow = [DogName, DogAge]
            StoredData.append(ListRow)
        elif (OptionVar == str(2)):
            print("******* The Current Dogs Available For Adoption Are [Name (Age)]: *******")
            for row in StoredData:
                print(row[0] + " (" + row[1] + ")")
            print("*******************************************")
        elif (OptionVar == str(3)):
            import pickle
            pickle_in = open("file.pickle", 'rb')
            StoredData = pickle.load(pickle_in)
            print("Reload Complete!")
            print("******* The Current Dogs Available For Adoption Are [Name (Age)]: *******")
            for row in StoredData:
                print(row[0] + " (" + row[1] + ")")
            print("*******************************************")
            print()
        elif (OptionVar == str(4)):
            print("Would you like to save & pickle your data?")
            Var3 = str(input("Enter 'y' or 'n' "))
            if (Var3 == str("y")):
                import pickle

                pickle_out = open("file.pickle", 'wb')
                pickle.dump(StoredData, pickle_out)
                pickle_out.close()
                continue
            elif (Var3 == str("n")):
                continue
        elif (OptionVar == str(5)):
            print("Would you like to exit the program?")
            Var4 = str(input("Enter 'y' or 'n' "))
            if (Var4 == str("y")):
                break
            elif (Var4 == str("n")):
                continue
    except ValueError:
        print("\nError: Invalid Input.")
        print("Please Ensure your Selection is Between [1] and [5]")
        print()
        continue
    except ZeroDivisionError:
        print("\nError: Invalid Input.")
        print("Please Ensure your Selection is Between [1] and [5]")
        print()
        continue
