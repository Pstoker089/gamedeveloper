

capitals={"England":"London",
          "France":"Paris",
          "Germany":"Berlin",
          "Russia":"Moscow"}

while True:
    
    choice=input("1) insert "
                 "2) display all countries "
                 "3) display all capitals "
                 "4) delete")
    if choice=="1":
        countryadd=input("Enter a country")
        capitaladd=input("enter a capital")
        capitals[countryadd]=capitaladd
    elif choice=="2":
        print(capitals)
    
    elif choice=="3":
        for i in capitals:
            print(capitals[i])
    elif choice=="4":
        delchoice=input("which country would you like to delete?")
        if delchoice in capitals:
            del capitals[delchoice]
        else:
            print("error")