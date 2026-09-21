from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 5


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 10


distance = 100

bus = Bus()
print("Bus Fare =", bus.calculate_fare(distance))

train = Train()
print("Train Fare =", train.calculate_fare(distance))

taxi = Taxi()
print("Taxi Fare =", taxi.calculate_fare(distance))

flight = Flight()
print("Flight Fare =", flight.calculate_fare(distance))