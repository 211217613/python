from abc import ABCMeta, abstractmethod

class Vehicle(object):
    """ A vehicle for sale """

    __metaclass__ = ABCMeta

    base_sale_price = 0

    def sale_price(self):
        if self.sold_on is None:
            return 0.0
        return 5000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
            return 0.0
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod #Now we can't create an instance of Vehicle
    def vehicle_type():
        """return a string representing the type of vehicle this is """
        pass

class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        return 'car'

class Truck(Vehicle):
    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        return 'Truck'
v = Vehicle()
