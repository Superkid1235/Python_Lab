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

# Customer Data Base
customer_list = [Customer("Caleb", "GOLD"),
                 Customer("David", "BRONZE"),
                 Customer("James", "SILVER")]

# Invoking a __str__ method
print(customer_list[0])             # try delete __str__ method to see different result
