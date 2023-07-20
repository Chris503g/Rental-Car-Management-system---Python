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


##  GET USER INPUT
def get_user_input(message, input_type=int):
    while True:
        try:
            return input_type(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid value.")


## DISPLAY CAR DETAILS
def display_car_details(cars):
    if len(cars) == 0:
        print("No cars to display.")
        return

    print("|", end="")
    for key in cars[0].keys():
        print(f"{key.upper(): <15}|", end="")
    print()

    for car in cars:
        print("|", end="")
        for value in car.values():
            if isinstance(value, bool):  # Check if value is a boolean
                value = str(value)  # Convert boolean to string
            print(f"{value: <15}|", end="")
        print()


## SHOW LIST OF CARS
def show_list_of_cars():
    if len(rental_cars) != 0:
        print("|", end="")
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


## SORTING BY KEY
def sort_by_key(sort_key):
    sorted_cars = sorted(rental_cars, key=lambda car: car[sort_key])
    display_car_details(sorted_cars)


## SHOW ALL AVAILABLE & UNAVAIBALE CARS
def show_available_cars(param):
    available_cars = [car for car in rental_cars if car["availability"] == param]
    display_car_details(available_cars)


## SCHEDULE MAINTENANCE FOR CARS
def schedule_maintenance():
    while True:
        print("==== SCHEDULE CAR MAINTENANCE ====")
        show_list_of_cars()

        # Get car ID
        car_id = get_user_input("Enter car ID: ", input_type=int)
        car_found = False

        for car in rental_cars:
            if car["car_id"] == car_id:
                car_found = True
                display_car_details([car])

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


## SORTING MENU
def sorting():
    while True:
        print("==== SORTING MENU ====")
        print(
            """ 
                1. By Brand (A --> Z)
                2. By Availability
                3. Back to Menu
                """
        )
        user_input = input("Enter your choice: ")
        # SORT BY BRAND
        if user_input == "1":
            sort_by_key("car_brand")

        # SORT BY AVAILABILITY
        elif user_input == "2":
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
        elif user_input == "3":
            return
        else:
            print("Invalid choice")
