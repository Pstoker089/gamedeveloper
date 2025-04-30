list=[]

for i in range(5):
    groupname=input("enter the name of the group: ")
    groupsize=input("Enter how many people were in the group: ")
    date=input("Enter the date of the competition: ")
    place=input("Enter where the venue is: ")
    medaltype=input("Enter the type of medal they got:")
    tuple1=(groupname,groupsize,date,place,medaltype)
    list.append(tuple1)


for i in list:
    print(i)

