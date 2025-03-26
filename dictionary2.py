
"""sentence=input("Enter a sentence: ").lower()

vowels={"a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0}

for letters in sentence:
    if letters in vowels:
        vowels[letters]+=1

print(vowels)"""


#pangram

import string

alphabets={}
for i in string.ascii_lowercase:
    alphabets[i]=0

sentence=input("Enter a sentence: ")

for letters in sentence:
    if letters in alphabets:
        alphabets[letters]+=1

pangram=True

for i in alphabets.values():
    if i==0:
        pangram=False
        break

if pangram:
    print("This sentence is a pangram")
else:
    print("This sentence isn't a pangram")