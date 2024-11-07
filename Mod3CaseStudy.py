"""
Author: Landon Ernst
File: Mod3CaseStudy.py
Date: November 7th, 2024
Description: This app will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes.
The app will then output the data in an easy-to-read and understandable format.
"""

#Superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Subclass Automobile that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  #Set vehicle type to "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

#Function to get car information from user
def get_car_info():
    #Get information from user
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or soft): ").lower()

    #Create the Automobile object
    car = Automobile(year, make, model, doors, roof)

    #Display the car information
    car.display_info()

#Run the app
get_car_info()
