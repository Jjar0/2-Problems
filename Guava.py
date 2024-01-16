def main():
    print ("Please select an activity from the following options:") #menu system
    print ("[1] Sorting Integers\n[2] Noughts and Crosses")
    menu = input ("[1/2]:")

    if menu == "1":
        print ("\n[SORTING INTEGERS]\n")
        int_sort()

    if menu == "2":
        print ("\n[NOUGHTS AND CROSSES]\n")
        noughts_crosses()

    else:
        print ("\nplease enter a listed number.\n")
        main()

def int_sort(): #problem 2 integer sort
    
    list = []
    listDone = False

    print ("Enter the integers you wish to be sorted,")
    print ("Once all numbers have been entered, enter 'exit' to continue.")

    while listDone != True: #loop for user to enter unlimited numbers
        userNum = input ("Enter a number:")

        if userNum == "exit":
            listDone = True

        try:
            userNum = float(userNum) #validation for user entered numbers
        except:
            print ("Please enter a numeric value,")
            continue

        userNum = float(userNum)

        list.append(userNum)
        print (str(userNum) + " added to list") #show user the number they entered

    bubble_sort(list) #calls sorting function

    print ("\nList of values in ascending order:") #prints list values in ascending order
    print(list)

    listMean = (sum(list)/len(list)) #Calculating mean of list

    print("\nMean of listed values:")
    print(str(listMean)+"\n")

    main()

def bubble_sort(list):

    length = len(list)

    for x in range(length-1): #iterate through the list
        for y in range(0, length-x-1):
  
            if list[y] > list[y+1]: #check if list is already swapped  
                list[y], list[y+1] = list[y+1], list[y] #swap elements
    
    return(list) #return to wider process

def noughts_crosses():
    
    
    
    main()

main()
   


