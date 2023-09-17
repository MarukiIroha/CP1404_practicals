from prac_09.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("good", 100, 90)
    bad_car = UnreliableCar("bad", 100, 10)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(10, 15):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()
