
"""list=[10,35,78,92,5,24,138]
print(len(list))
print(list[3])
print(list[2:6])
print(list[5:1:-1])

matrix=[[5,6,7],[3,6,9],[4,6,8]]
print(len(matrix))
print(len(matrix[2]))
print(matrix[1][2])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()"""

#making a matrix through inputs

"""colums=int(input("Enter the number of colums"))
rows=int(input("Enter the number of rows"))

matrix=[]
for i in range(rows):
    temp=[]
    for i in range(colums):
        value=int(input("Enter the value: "))
        temp.append(value)
    matrix.append(temp)

print(matrix)"""

#adding values in a matrix

"""matrix1=[[1,5],[2,10]]
matrix2=[[3,6],[2,4]]
matrix3=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
print(matrix3)"""

#Get 20 random marks for 20 students (between 0 to 100). 
# Create 3 separate lists . 
# The first list should contain the marks <=30.
#  The second list between 31 to 69. 
# The third list >= 70.

from random import randint

list1=[]
list2=[]
list3=[]
matrix=[]

for i in range(20):
    number=randint(0,100)
    if number<=30:
        list1.append(number)
    elif number>31 and number<70:
        list2.append(number)
    else:
        list3.append(number)

matrix.append(list1)
matrix.append(list2)
matrix.append(list3)

print(matrix)
