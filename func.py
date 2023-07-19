# Imports
import datetime
import json

# Read the contents of the JSON file
with open("rental_cars.json") as file:
    json_data = file.read()

# Parse the JSON data into Python objects
rental_cars = json.loads(json_data)

under_maintenance = [{"car_id": 1, "date": 2023 - 4 - 15, "description": "Overhaul"}]


## CONFIRMATION PAGE
def confirmation_page():
    print("==== CONFIRMATION PAGE ====")
    print(
        """ Do you want to continue?
        1. Yes
        2. No
        """
    )
    user_input = input("Enter choice: ")
    return user_input


## SHOW LIST OF CARS
def show_list_of_cars():
    if len(rental_cars) != 0:
        for key in rental_cars[0].keys():
            print(f"{key.upper() :<15}|", end="")
        print()

        for car in rental_cars:
            print("|", end="")
            for value in car.values():
                if isinstance(value, bool):  # Check if value is a boolean
                    value = str(value)  # Convert boolean to string
                print(f"{value:<15}|", end="")
            print()
    else:
        print("No data in rental car")


## SHOW ALL AVAILABLE & UNAVAIBALE CARS
def show_available_cars(param):
    available_cars = [car for car in rental_cars if car["availability"] == param]
    if available_cars:
        print("|", end="")
        for key in available_cars[0].keys():
            print(f"{key.upper(): <15}|", end="")
        print()

        for car in available_cars:
            print("|", end="")
            for value in car.values():
                if isinstance(value, bool):  # Check if value is a boolean
                    value = str(value)  # Convert boolean to string
                print(f"{value: <15}|", end="")
            print()
    else:
        print("No available cars")


## SORTING MENU
def sorting():
    while True:
        print("==== SORTING MENU ====")
        print(
            """ 1. By Brand (A --> Z)
                2. By Price
                3. By Availability
                4. Back to Menu
                """
        )
        user_input = input("Enter your choice: ")
        # SORT BY BRAND
        if user_input == "1":
            sort_by_key(user_input)

        # SORT BY RENTAL PRICE
        elif user_input == "2":
            sort_by_key(user_input)

        # SORT BY AVAILABILITY
        elif user_input == "3":
            print("==== SORT BY AVAILABILITY MENU ====")
            print(
                """
                  1. Available
                  2. Unavailable
                  3. Back 
                  """
            )
            avail_input = input("Enter your choice: ")
            if avail_input == "1":
                show_available_cars(True)
            elif avail_input == "2":
                show_available_cars(False)
            else:
                print("Invalid choice")
        elif user_input == "4":
            return
        else:
            print("Invalid choice")


def sort_by_key(num):
    # SORT BY BRAND
    if num == "1":
        sorted_cars = sorted(rental_cars, key=lambda car: car["car_brand"])
    # SORT BY PRICE
    elif num == "2":
        sorted_cars = sorted(
            rental_cars, key=lambda car: car["rental_price"], reverse=True
        )

    # Print the sorted cars
    print("|", end="")
    for key in sorted_cars[0].keys():
        print(f"{key.upper(): <15}|", end="")
    print()

    for car in sorted_cars:
        print("|", end="")
        for value in car.values():
            if isinstance(value, bool):  # Check if value is a boolean
                value = str(value)  # Convert boolean to string
            print(f"{value: <15}|", end="")
        print()


## SCHEDULE MAINTENANCE FOR CARS
def schedule_maintenance():
    while True:
        print("==== SCHEDULE CAR MAINTENANCE ====")
        show_list_of_cars()

        # Get car ID
        while True:
            try:
                car_id = int(input("Enter Car ID for maintenance: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid car ID")

        car_found = False

        for car in rental_cars:
            if car["car_id"] == car_id:
                car_found = True

                print("|", end="")
                for key in car.keys():
                    print(f"{key: <15}|", end="")
                print()
                print("|", end="")

                for value in car.values():
                    if isinstance(value, bool):  # Check if value is a boolean
                        value = str(value)  # Convert boolean to string
                    print(f"{value: <15}|", end="")
                print()

                # Schedule maintenance for the selected car
                print("==== MAINTENANCE FORM ====")

                maintenance_date = datetime.date.today().strftime("%Y-%m-%d")
                print(f"Maintenance Date = {maintenance_date}")
                maintenance_desc = input("Enter a description of the maintenance: ")

                maintenance_data = {
                    "car_id": car_id,
                    "date": maintenance_date,
                    "description": maintenance_desc,
                }
                under_maintenance.append(maintenance_data)
                print("Maintenance scheduled successfully.")
                break

        if not car_found:
            print("Car not found. Please enter a valid car ID.")

        break  # Exit the loop after scheduling maintenance


## VIEW CARS UNDER MAINTENANCE
def view_maintenance():
    print("==== CAR UNDER MAINTENANCE ====")

    if len(under_maintenance) == 0:
        print("No car under maintenance right now")
    else:
        print("|", end="")
        for key in under_maintenance[0].keys():
            print(f"{key:<15}|", end="")
        print()

        for maintenance_data in under_maintenance:
            print("|", end="")
            print(f"{maintenance_data['car_id']:<15}|", end="")
            print(f"{maintenance_data['date']:<15}|", end="")
            print(f"{maintenance_data['description']}")


## MAINTENANCE MENU
def maintenance_menu():
    print("==== MAINTENANCE MENU ====")
    print(
        """
          1. Schedule maintenance 
          2. View maintenance 
          3. Back
          """
    )
    user_input = input("Enter your choice: ")

    if user_input == "1":
        schedule_maintenance()
    elif user_input == "2":
        view_maintenance()
    elif user_input == "3":
        return
    else:
        print("Invalid choice")
