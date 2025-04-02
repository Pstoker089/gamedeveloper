
with open("test.txt","w") as store:
    store.write("Hello world!!")



with open("test.txt","a") as store:
    store.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.")

with open("test.txt","r") as store:
    print(store.readline(10))