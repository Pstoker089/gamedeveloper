"""print("hello world")

capitals={"USA":"Washington DC",
          "England":"London",
           "France":"Paris",
            "Russia":"Moscow",
             "Germany":"Berlin",
              "Spain":"Madrid",
               "Italy":"Rome" }

print(len(capitals))

print(capitals["Germany"])
print(capitals.get("India","Not in the dictionary"))
print(capitals.values())
for i,j in capitals.items():
    print(i,j)

for i in capitals:
    print(i,capitals[i])

print("India" in capitals)"""


games={"Minecraft":"Sandbox",
       "Fortnite":"3rd person shooter",
       "Mario":"2d platformer",}

choice=input("pick a game ").capitalize()
if choice not in games:
    print("INVALID GAME")
else:
    print(games[choice])

games["Chess"]="Strategy"

for i in games:
    print(i,games[i])