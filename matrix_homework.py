colums=int(input("Enter the number of colums and rows: "))

matrix=[]
for i in range(colums):
    temp=[]
    for i in range(colums):
        value=int(input("Enter the value: "))
        temp.append(value)
    matrix.append(temp)

for i in range(colums):
    print(matrix[i][i])

