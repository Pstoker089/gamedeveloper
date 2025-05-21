import string

letters=set(string.ascii_lowercase)

pangram=True

sequence=input("input a sentence: ")
for i in letters:
    if i not in sequence:
       pangram=False
       break
if pangram:
    print("This sentence is a pangram")
else:
    print("This sentence isn't a pangram")
