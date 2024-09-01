class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        #Printing out the car's information
        print(f"Car Information: Make - {self.make}, Model - {self.model}, Year - {self.year}")
