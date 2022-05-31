class Customer():
    def __init__(self,name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        self.membership_type = new_membership


c = Customer("Caleb",  "Gold")
c2 = Customer("Brad", "Bronze")


customer_list = [Customer("Caleb", "GOLD"),
                 Customer("David", "BRONZE"),
                 Customer("James", "SILVER")]




