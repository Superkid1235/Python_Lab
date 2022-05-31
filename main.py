class Customer():
    def __init__(self,name, membership_type):
        self.name = name
        self.membership_type = membership_type

    # static method (not attached to an object)
    def read_customer():
        print("this static method >> read_customer() has been invoked")

# Customer Data Base
customer_list = [Customer("Caleb", "GOLD"),
                 Customer("David", "BRONZE"),
                 Customer("James", "SILVER")]

# invoking a static method read_customer():
Customer.read_customer()