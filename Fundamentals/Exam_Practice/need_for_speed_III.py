def drive(car_keys, key_car, given_distance, needed_fuel):
    if needed_fuel > car_keys["fuel"]:
        print("Not enough fuel to make that ride")
    else:
        car_keys["mileage"] += given_distance
        car_keys["fuel"] -= needed_fuel
        print(f"{key_car} driven for {given_distance} kilometers. {needed_fuel} liters of fuel consumed.")
    return car_keys


def refuel(car_dict_fuel, refuel_car, fuel_quantity):
    max_capacity = 75
    if car_dict_fuel + fuel_quantity > max_capacity:
        fuel_quantity = max_capacity - car_dict_fuel
        car_dict_fuel = max_capacity
    else:
        car_dict_fuel += fuel_quantity
    print(f"{refuel_car} refueled with {fuel_quantity} liters")
    return car_dict_fuel


def revert(mileage, car, kilometers):
    mileage -= kilometers
    if mileage < 10000:
        mileage = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return mileage


number_of_cars = int(input())

car_dictionary = {}
for cars in range(number_of_cars):
    car_info = input().split("|")
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    car_dictionary[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input().split(" : ")

    if command[0] == "Stop":
        break

    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        car_dictionary[car] = drive(car_dictionary[car], car, distance, fuel)
        if car_dictionary[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del car_dictionary[car]

    elif command[0] == "Refuel":
        refuel_tank = int(command[2])
        car_dictionary[car]["fuel"] = refuel(car_dictionary[car]["fuel"], car, refuel_tank)

    elif command[0] == "Revert":
        kilometers = int(command[2])
        car_dictionary[car]["mileage"] = revert(car_dictionary[car]["mileage"], car, kilometers)

for left_cars in car_dictionary.keys():
    print(f"{left_cars} -> Mileage: "
          f"{car_dictionary[left_cars]['mileage']} kms,"
          f" Fuel in the tank: {car_dictionary[left_cars]['fuel']} lt.")
