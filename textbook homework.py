
textbooks={"History":300,
           "Maths":160,
           }

while True:
    choice=input("What would you like to do? \n1. add a textbook \n2. edit a cost"
    "\n3. show a specific cost \n4. show the total cost \n5. exit \n")

    if choice=="1" or choice=="add a textbook":
        addbook=input("enter the book you would like to add: ")
        addvalue=input("enter the cost of the new book: ")
        textbooks[addbook]=addvalue
    elif choice=="2" or choice=="edit a price":
        editchoice=input("Which book's price would you like to edit? ")
        editprice=input("What would you like to change the cost to? ")
        textbooks[editchoice]=editprice
    elif choice=="3" or choice=="show a specific cost":
        showchoice=input("Which textbook's cost would you like to show? ")
        print(textbooks[showchoice])
    elif choice=="4" or choice=="show the total cost":
        total=0
        for i in textbooks.values():
            total+=i
        print(total)
    elif choice=="5" or choice=="exit":
        break