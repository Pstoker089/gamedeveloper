
numbers={"1":0,
"2":0,
"3":0,
"4":0,
"5":0,
"6":0,
"7":0,
"8":0,
"9":0,
"0":0}

sequence=input("Enter a sequence of numbers: ")

for i in sequence:
    if i in numbers:
        numbers[i]+=1
pangram=True
for j in numbers.values():
    if j==0:
        pangram=False
if pangram:
    print("This sequence is a a pangram")
else:
    print("This sequence is not a pangram")
