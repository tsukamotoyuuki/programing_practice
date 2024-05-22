class Car:
    def __init__(self, seats, max_speed):
        self.__seats = seats
        self.__max_speed = max_speed

    def spec(self):
        print(F"\nseats : {self.__seats}, max_speed = {self.__max_speed}", end="")

    @property
    def seats(self):
        return self.__seats

    @property
    def max_speed(self):
        return self.__max_speed

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.__dict__ == other.__dict__


class Truck(Car):
    def __init__(self, seats, max_speed, capacity):
        super().__init__(seats, max_speed)
        self.__capacity = capacity

    def spec(self):
        super().spec()
        print(F", capacity : {self.__capacity}")


a = Car(6, 100)
b = Car(1, 300)
c = Truck(2, 100, 50)
print(a.seats)
a.spec()
b.spec()
c.spec()
a2 = Car(6, 100)
c2 = Truck(2, 100, 50)
print(a == a2)
print(c == c2)