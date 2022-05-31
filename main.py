class Customer():
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.customer_database = []

    # string method
    def __str__(self):
        return self.name + " : " + str(self.points)

    # static function
    def show_all_customers(customer_database):
        for customer in customer_database:
            print(customer)


customer_database = [Customer("James", 32),
                     Customer("Steve", 12),
                     Customer("Keith", 59),
                     Customer("George", 40),
                     Customer("Nomatak", 68),
                     Customer("Dewey", 1)]

Customer.show_all_customers(customer_database)