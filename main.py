class Customer():
    def __init__(self,name, membership_type):
        self.name = name
        self.membership_type = membership_type

    # static method (invoke by a class itself, not an object of a class)
    def read_customer():
        print("this static method >> read_customer() has been invoked")

    # string method __str__
    def __str__(self):
        return self.name + " " + self.membership_type

    # static function
    def print_all_customer(customer_list):
        for customer in customer_list:
            print(customer)

# Customer Data Base
customer_list = [Customer("Caleb", "GOLD"),
                 Customer("David", "BRONZE"),
                 Customer("James", "SILVER")]

# Invoking Static Function print_all_customer()
Customer.print_all_customer(customer_list)