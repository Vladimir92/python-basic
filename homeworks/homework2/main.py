from homeworks.homework2.vehicle import *

try:
    audi = Car(500, 10, 500, 45, 50, Engine(95))
    print(f"Car audi created: {audi}")
    audi.move(55)
    audi.move(40)
    audi.move(40)
    audi.signal()

    print()
    ferrari = SportCar(800, 0, 400, 50, 70, SportEngine(600, 'front', 1000))
    print(f"Sport car ferrari created: {ferrari}")
    ferrari.move(10)
    ferrari.move(20)
    ferrari.signal()

    print()
    airbus = Plane(9000, 150, 4000, 500, 700, AvionicEngine(900, 8_000, 0.6))
    print(f"Airbus plane created: {airbus}")
    airbus.move(500)
    airbus.move(300)
    airbus.signal()

    print()
    su37 = Fighter(9000, 1, 2, 500, 700, AvionicEngine(95000, 10_000, 0.8), Weaponry(4, 2000, 20))
    print(f"SU37 patrol fighter created: {su37}")
    su37.move(2500)
    su37.move(1300)
    su37.signal()

    print()
    print("Trying to initialize wrong Plane..")
    wr_plane = Plane(-1, 0, 0, 0, -1, None)
except NegativeParameterError as e:
    print(e)

except TypeError as t:
    print(t)

try:
    print()
    print("Trying to create car without engine")
    audi = Car(500, 10, 500, 45, 50, None)
    print(f"Car audi created: {audi}")
    audi.move(55)
except TypeError as t:
    print(t)

try:
    print()
    print("Trying to move on car that have low petrol")
    audi.refuel(10)
    audi.move(55)
except TypeError as t:
    print(t)

try:
    print()
    print("Trying to crete fighter with wrong engine")
    mig32 = Fighter(9000, 150, 4000, 500, 700, AvionicEngine(95000, 10_000, 0.0), Weaponry(0, 2000, 20))
except NegativeParameterError as e:
    print(e)
except TypeError as t:
    print(t)

try:
    print()
    print("Trying to load plane with extra amount of passengers")
    airbus370 = Plane(9000, 150, 300, 500, 700, AvionicEngine(900, 8_000, 0.6))
    airbus370.add_passengers(5)
    airbus370.rm_passengers(10)
    airbus370.add_passengers(500)
except NegativeParameterError as e:
    print(e)
except TypeError as t:
    print(t)

try:
    print()
    print("Trying to set unproper weight to fighter")
    mig33 = Fighter(9000, 1, 2, 500, 700, AvionicEngine(95000, 10_000, 0.5), Weaponry(0, 2000, 20))
    mig33.weight = 10000
except NegativeParameterError as e:
    print(e)
except TypeError as t:
    print(t)

try:
    print()
    print("Trying to equip plane with 4 pilots")
    mig25 = Fighter(9000, 1, 2, 500, 700, AvionicEngine(95000, 10_000, 0.5), Weaponry(0, 2000, 20))
    mig25.max_carry = 4
except NegativeParameterError as e:
    print(e)
except ValueError as v:
    print(v)
