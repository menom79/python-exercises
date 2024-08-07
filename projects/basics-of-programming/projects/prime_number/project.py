# Project for Basics of programmming.
# Get insurance on your vehicle purchase.

import sys

class Customer(object):
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
    
    def get_insurange_rate(self):
        if self.gender.lower() == 'm' or self.gender.lower() == 'male':
            if self.age >= 15 and self.age < 25:
                return 25
            if self.age >= 25 and self.age < 40:
                return 17
            if self.age >= 40 and self.age < 70:
                return 10
        
        if self.gender.lower() == 'f' or self.gender.lower() == 'female':
            if self.age >= 15 and self.age < 25:
                return 20
            if self.age >= 25 and self.age < 40:
                return 15
            if self.age >= 40 and self.age < 70:
                return 10
        return None
    
    def get_monthly_insurance(self, vehicle_purchase_price):
        insurance_rate = self.get_insurange_rate()
        if insurance_rate:
            monthly_insurance = vehicle_purchase_price * insurance_rate / (100 * 12)
            return monthly_insurance
        return 0.0


    
def main():    
    # Ask user for gender.
    genders = ['f', 'female', 'm', 'male']
    gender = input("Enter yout gender (M/F): ")
    if gender.lower() not in genders:
        print('Incorrect gender. Please enter female, male, f or m.')
        sys.exit()
    age = int(input("Your age: "))
    if age < 15 or age >= 70:
        print('You are not eligible for insurance according to our policy.')
        sys.exit()
    vehicle_purchase_price = float(input("Enter the purchase price of the vehicle: $"))
    customer = Customer(age, gender)

    monthly_insurance = customer.get_monthly_insurance(vehicle_purchase_price)
    print("Your monthly insurance will be: ${0:.2f}".format(monthly_insurance))


if __name__ == "__main__":
    main()

