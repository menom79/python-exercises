# Project for Basics of programmming.

# Get insurance for your vehicle.

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
    
    def get_monthly_insurance(self, vehicle_purchase_price):
        insurance_rate = self.get_insurange_rate()
        monthly_insurance = vehicle_purchase_price * insurance_rate / (100 * 12)
        return monthly_insurance


    
def main():    
    # Ask user for gender.
    gender = input("Enter yout gender (M/F): ")
    age = int(input("Your age?: "))
    vehicle_purchase_price = float(input("Enter the purchase price of the vehicle: $"))
    customer = Customer(age, gender)

    monthly_insurance = customer.get_monthly_insurance(vehicle_purchase_price)
    print("Your monthly insurance will be: ${0:.2f}".format(monthly_insurance))


if __name__ == "__main__":
    main()

