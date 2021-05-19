class Car():
    """Простая модель автомобиля."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        bt_range = 0
        if self.battery_size == 75:
            bt_range = 260
        elif self.battery_size == 100:
            bt_range = 315
        print(f"This car can go about {bt_range} miles on a full charge.")

    # New method: task 09.9
    def upgrade_battery(self, new_value=100):
        print(f"Battery size is {self.battery_size}")
        print("Upgrading...")
        if self.battery_size < 100:
            self.battery_size = new_value
        return f"Battery upgraded to {self.battery_size}"


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты класса-родителя. Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


# test from the book
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# test 09.9
print("=====")
print(my_tesla.battery.upgrade_battery())  # 100
my_tesla.battery.battery_size = 50
print(my_tesla.battery.upgrade_battery(90))  # 90
print("-----")
prius = ElectricCar('toyota', 'prius', 2020)
prius.battery.describe_battery()
prius.battery.get_range()
print(prius.battery.upgrade_battery())
prius.battery.get_range()
