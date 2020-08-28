import random

from homeworks.homework2.components import Engine, AvionicEngine, SportEngine, Weaponry
from homeworks.homework2.exceptions import NegativeParameterError
from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):

    @property
    @abstractmethod
    def weight(self):
        raise NotImplementedError

    @weight.setter
    @abstractmethod
    def weight(self, val):
        raise NotImplementedError

    @property
    @abstractmethod
    def carrying(self):
        raise NotImplementedError

    @carrying.setter
    @abstractmethod
    def carrying(self, val):
        raise NotImplementedError

    @abstractmethod
    def signal(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def move(self, distance) -> int:
        raise NotImplementedError


class Car(Vehicle):

    def __init__(self, weight=1000, carrying=0, max_carry=400, petrol=50, fuel_capacity=50, engine=Engine(90)):
        if weight < 0:
            raise NegativeParameterError("Weight cannot be negative", weight)
        self._weight = weight
        self._carrying = carrying
        self._max_carry = max_carry
        self._petrol = petrol
        self._fuel_capacity = fuel_capacity
        if not isinstance(engine, Engine):
            raise TypeError("Car must be init with proper Engine instance")
        self._engine = engine

    def __str__(self):
        return f"Car of weight {self._weight}, carry {self._carrying} of {self._max_carry}. Have {self._petrol} of {self._fuel_capacity}. Engine {self._engine}"

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, val):
        if val < 0:
            raise NegativeParameterError("Weight cannot be negative", val)
        self._weight = val

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, val):
        if val < 0:
            raise NegativeParameterError("Carrying amount cannot be negative", val)
        self._carrying = val

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        if not isinstance(engine, Engine):
            raise TypeError("Car must be init with proper Engine instance")
        self._engine = engine

    @property
    def petrol(self):
        return self._petrol

    def refuel(self, amount=0):
        if amount < 0:
            raise NegativeParameterError("Cannot fuel with negative amount of petrol", amount)
        new_fuel = self._petrol + amount
        if new_fuel > self._fuel_capacity:
            print(f"Fueled full tank of {self._fuel_capacity}l, extra petrol {new_fuel - self._fuel_capacity}l is lost")
            self._petrol = self._fuel_capacity
            return self._petrol
        print(f"Fueled car with {amount} litres, Now have {self._petrol + amount} litres")
        self._petrol += amount
        return self._petrol

    def signal(self):
        print("Car beeps!")

    def load(self, amount):
        if amount < 0:
            raise NegativeParameterError("Cannot load with negative weight", amount)
        if self._carrying + amount > self._max_carry:
            print(f"Unable to load {amount}. Carry limit of {self._max_carry} reached. Current load {self._carrying}")
            return
        self._carrying += amount
        return self._carrying

    def unload(self, amount):
        if amount < 0:
            raise NegativeParameterError("Cannot remove negative weight from Car", amount)
        if self._carrying - amount < 0:
            print(f"Unable to unload {amount}. Car does not have such cargo. Removing all existing cargo")
            self._carrying = 0
            return self._carrying
        self._carrying -= amount
        return self._carrying

    def move(self, distance):
        rq_petrol = round((distance - 0.01 * self._weight + 0.15 * self._carrying) / self._engine.get_coef())
        if self._petrol < rq_petrol:
            print(f"Not enough fuel to drive {distance}, required petrol {rq_petrol}, current petrol {self._petrol}")
            return
        self._petrol -= rq_petrol
        print("Driving", distance, ", petrol left", self._petrol)
        self._petrol = round(self._petrol)
        return self._petrol


class Plane(Vehicle):

    def __init__(self, weight=10000, carrying=0, max_carry=4000, kerosene=500, fuel_capacity=700,
                 engine=AvionicEngine(800, 9_000, 0.6)):
        if weight < 0:
            raise NegativeParameterError("Weight cannot be negative", weight)
        self._weight = weight
        self._carrying = carrying
        self._max_carry = max_carry
        self._kerosene = kerosene
        self._fuel_capacity = fuel_capacity
        if not isinstance(engine, AvionicEngine):
            raise TypeError("Plane must be init with proper AvionicEngine instance")
        self._engine = engine

    def __str__(self):
        return f"Plane of weight {self._weight}, carry {self._carrying} of {self._max_carry}. Have {self._kerosene} of {self._fuel_capacity}. Engine {self._engine}"

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, val):
        if val < 0:
            raise NegativeParameterError("Weight cannot be negative", val)
        if val > 10 * self._max_carry:
            print(f"Plane cannot weight more than 10 * carry_cap ({10 * self._max_carry}). Setting max weight")
            self._weight = 10 * self._max_carry
        self._weight = val

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, val):
        if val < 0:
            raise NegativeParameterError("Carrying amount cannot be negative", val)
        self._carrying = val

    def signal(self) -> None:
        print("Plane whoofs!")

    def add_passengers(self, amount):
        if amount < 0:
            raise NegativeParameterError("Cannot get negative amount on board", amount)
        if self._carrying + amount > self._max_carry:
            print(f"Unable to load {amount} passengers. Plane carry limit of {self._max_carry} reached. Current load {self._carrying}")
            return
        self._carrying += amount
        print(f"Loaded {amount} passengers to plane. Current cap {self._carrying} of {self._max_carry}")
        return self._carrying

    def rm_passengers(self, amount):
        if amount < 0:
            raise NegativeParameterError("Cannot remove negative amount of people from board", amount)
        if self._carrying - amount < 0:
            print(f"Unable to rm {amount}. There are not enough on board. Removing all passengers")
            self._carrying = 0
            return self._carrying
        self._carrying -= amount
        print(f"Removed {amount} passengers from plane. Current cap {self._carrying} of {self._max_carry}")
        return self._carrying

    def move(self, distance) -> int:
        rq_kerosene = round((distance + 0.25 * self._weight + 0.1 * self._carrying) / self._engine.get_fly_coef(), 2)
        print(f"rq_kerosene {rq_kerosene}, coef {self._engine.get_fly_coef()}")
        if self._kerosene < rq_kerosene:
            print(f"Not enough kerosene to fly {distance}, required is {rq_kerosene}, current amount: {self._kerosene}")
            return 0
        self._kerosene -= rq_kerosene
        self._kerosene = round(self._kerosene, 2)
        print("Flying", distance, ", kerosene left", self._kerosene)
        return self._kerosene


class SportCar(Car):
    def __init__(self, weight=800, carrying=0, max_carry=300, petrol=40, fuel_capacity=70,
                 engine=SportEngine(300, 'front', 2000)):
        super().__init__(weight, carrying, max_carry, petrol, fuel_capacity)
        if not isinstance(engine, SportEngine):
            raise TypeError("Sport car must be init with proper SportEngine instance")
        self._engine = engine

    def __str__(self):
        return f"Sport Car of weight {self._weight}, carry {self._carrying} of {self._max_carry}. Have petrol {self._petrol} of {self._fuel_capacity}. Engine {self._engine}"

    @property
    def engine(self):
        return self._engine

    @Car.engine.setter
    def engine(self, engine):
        if not isinstance(engine, SportEngine):
            raise TypeError("Sport car must be init with proper SportEngine instance")
        self._engine = engine

    @Car.weight.setter
    def weight(self, val):
        if val < 0:
            raise NegativeParameterError("Weight cannot be negative", val)
        if val > 3 * self._max_carry:
            print(f"SportCar cannot weight more than 3 * carry_cap ({10 * self._max_carry}). Setting max weight")
            self._weight = 3 * self._max_carry
        self._weight = val

    def move(self, distance):
        rq_petrol = round((distance + 0.02 * self._weight + 0.25 * self._carrying) / self._engine.get_race_coef(), 3)
        print(f"rq_petrol {rq_petrol}, wd_coef {self._engine.get_race_coef()}")
        if self._petrol < rq_petrol:
            print(f"Not enough fuel to race {distance}, required petrol {rq_petrol}, current petrol {self._petrol}")
            return
        self._petrol -= rq_petrol
        print("Racing", distance, ", petrol left", self._petrol)
        self._petrol = round(self._petrol)
        return self._petrol


class Fighter(Plane):

    def __init__(self, weight=6000, carrying=1, max_carry=2, kerosene=400, fuel_capacity=600,
                 engine=AvionicEngine(900, 10_000, 0.6),
                 weapons=Weaponry(4, 2000, 15)):
        if max_carry > 2:
            raise ValueError(f"Fighter cannot carry more than 2 pilots, got {max_carry}")
        super().__init__(weight, carrying, max_carry, kerosene, fuel_capacity, engine)
        if not isinstance(weapons, Weaponry):
            raise TypeError("Fighter can carry only instances of Weaponry class")
        self._weapons = weapons

    def __str__(self):
        return f"Fighter plane of weight {self._weight}, carry {self._carrying} of {self._max_carry}. Have fuel {self._kerosene} of {self._fuel_capacity}. Engine {self._engine}. Weaponry {self._weapons}"

    @property
    def weapons(self):
        return self._weapons

    @weapons.setter
    def weapons(self, wpn):
        if not isinstance(wpn, Weaponry):
            raise TypeError("Fighter can carry only instances of Weaponry class")
        self._weapons = wpn
        return

    @property
    def max_carry(self):
        return self._max_carry

    @max_carry.setter
    def max_carry(self, val):
        if val < 0:
            raise NegativeParameterError("Carrying amount cannot be negative", val)
        if val > 2:
            raise ValueError(f"Fighter cannot carry more than 2 pilots, got {val}")
        self._max_carry = val

    @Plane.weight.setter
    def weight(self, val):
        if val < 0:
            raise NegativeParameterError("Weight cannot be negative", val)
        if val > 3 * self._max_carry:
            print(f"Plane cannot weight more than 500 * carry_cap ({500 * self._max_carry}). Setting max weight")
            self._weight = 3 * self._max_carry
        self._weight = val

    def move(self, distance) -> int:
        rq_kerosene = round((distance + 0.3 * self._weight + 0.4 * self._carrying) / self._engine.get_fly_coef(), 2)
        print(f"rq_kerosene {rq_kerosene}, coef {self._engine.get_fly_coef()}")
        if self._kerosene < rq_kerosene:
            print(f"Not enough kerosene to patrol {distance}, required is {rq_kerosene}, current amount: {self._kerosene}")
            return 0
        rand_enemies = random.randint(0, 5)
        if not self.fight(rand_enemies):
            print("Cannot move further... Load more ammo.")
            return 0
        self._kerosene -= rq_kerosene
        self._kerosene = round(self._kerosene)
        print("Patrolling", distance, ", kerosene left", self._kerosene)
        return self._kerosene

    def fight(self, enemies):
        if enemies < 0:
            raise NegativeParameterError("Amount of enemies cannot be negative", enemies)
        if enemies == 0:
            print("Clear skies. No enemies, continue patrol")
            return True
        if self._weapons.fight(enemies):
            return True
        return False
