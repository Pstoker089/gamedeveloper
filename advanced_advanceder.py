while True:
    choice=input("---WELCOME TO THE JOURNAL APP---\n1. Write an entry\n2. View all entries\n3. Exit\n").lower()
    if choice=="1" or choice=="write an entry":
        entry=input("Write your entry: ")
        with open("entry.txt","a") as file:
           file.write(entry)
        print("ENTRY SAVED")
    elif choice=="2" or choice=="view all entries":
        with open("entry.txt","r") as file:
            index=1
            for i in file:
                print(index,i)
                print("\n")
                index+=1
    elif choice=="3" or choice=="exit":
        break
    else:
        print("INVALID CHOICE")
            