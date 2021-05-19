class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def print_served_visitors(business):
        print("Current number of served visitors:", business.number_served)

    def describe_restaurant(self):
        answer = f"Hello! Our restaurant \"{self.restaurant_name}\" is serving {self.cuisine_type} cuisine"
        return answer

    def open_restaurant(self):
        print("Welcome, dear visitors!")

    def set_number_served(self, visitors_served):
        self.number_served = visitors_served

    def increment_number_served(self, increment_served):
        self.number_served += abs(int(increment_served))


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'vanilla', 'chocolate', 'lemon'
        self.number_served = 100

    def set_flavors(self, *flavors):
        self.flavors += flavors
        return self.flavors

    def get_flavors(self):
        res = []
        for flavor in self.flavors:
            res.append(flavor)
        return res


# test task 09.6
ice_cream_stand = IceCreamStand('Kiosk 3rd Ave', 'ice cream')
print(ice_cream_stand.describe_restaurant())
print(*ice_cream_stand.get_flavors())  # vanilla chocolate lemon
print(ice_cream_stand.number_served)  # 100
ice_cream_stand.increment_number_served(25)
print(ice_cream_stand.number_served)  # 125
ice_cream_stand2 = IceCreamStand('Kiosk 11th Ave', 'ice cream plus')
print(ice_cream_stand2.describe_restaurant())
print(ice_cream_stand2.set_flavors('orange', 'tea rose', 'tiramisu'))
