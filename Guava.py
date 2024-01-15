def main():
    print ("Please select an activity from the following options:")
    print ("[1] Sorting Integers\n[2] Noughts and Crosses")
    menu = input ("[1/2]:")

    if menu == "1":
        print ("\n[SORTING INTEGERS]\n")
        intsort()

    if menu == "2":
        print ("\n[NOUGHTS AND CROSSES]\n")
        noughts()

    else:
        print ("\nplease enter a listed number.\n")
        main()

def intsort():
    
    list = []
    listDone = False

    print ("Enter the integers you wish to be sorted,")
    print ("Once all numbers have been entered, enter 'exit' to continue.")

    while listDone != True:
        userNum = input ("Enter a number:")

        if userNum == "exit":
            listDone = True

        try:
            userNum = float(userNum)
        except:
            print ("Please enter a numeric value,")
            continue

        userNum = float(userNum)

        list.append(userNum)
        print (str(userNum) + " added to list")

    print ("\nun-sorted list:")
    print (list)




    
    main()

def noughts():
    
    
    
    main()

main()
   


