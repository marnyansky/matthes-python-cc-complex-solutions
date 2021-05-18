def make_car(manufacturer, model, **car): # normal name is **kwargs
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car


# Test
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
