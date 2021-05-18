class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def print_served_visitors(business):
        print("Current number of served visitors:", business.number_served)

    def describe_restaurant(self):
        print(f"Hello! Our restaurant \"{self.restaurant_name}\" is serving {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print("Welcome, dear visitors!")

    def set_number_served(self, visitors_served):
        self.number_served = visitors_served

    def increment_number_served(self, increment_served):
        self.number_served += abs(int(increment_served))


# test task 09.1
restaurant = Restaurant("NYC", "American")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# test task 09.4
r_new = Restaurant("Cappuccino", "Italian")
r_new.print_served_visitors()

r_new.number_served = 5
r_new.print_served_visitors()

r_new.set_number_served(10)
r_new.print_served_visitors()

r_new.increment_number_served(2)
r_new.print_served_visitors()
