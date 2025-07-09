class car:
    def __init__(self, brand, model, colour):
        self.brand=brand
        self.model=model
        self.colour=colour
    def printer(self):
        print(f"the brand of car is {self.brand}")
        print(f"the model of car is {self.model}")
        print(f"the colour of the car is {self.colour}")

c1=car("Ford","F150","Red")
c1.printer()