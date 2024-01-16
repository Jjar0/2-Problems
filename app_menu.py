from integer_sorting import int_sort

while True:
    print ("\nPlease select an activity from the following options:") #menu system
    print ("[1] Sorting Integers\n[2] Noughts and Crosses")
    menu = input ("[1/2]:")

    if menu == "1":
        print ("\n[SORTING INTEGERS]")
        int_sort()

    if menu == "2":
        print ("\n[NOUGHTS AND CROSSES]\n")
        
    else:
        print ("\nplease enter a listed number.\n")
        continue




