from func import *


## SHOW LIST OF CARS
def show_cars():
    while True:
        print("\t\t==== SHOW RENTAL CAR MENU ====")
        print(
            """
              1. Show all Rental Cars
              2. Check a Rental Car 
              3. Back to Menu
              """
        )
        user_input = input("Enter your choice: ")
        # 1. SHOW ALL RENTAL CARS
        if user_input == "1":
            # CHECK IF rental_car data exist
            if len(rental_cars) != 0:
                # Assuming all dictionaries have the same keys
                show_list_of_cars()
            else:
                print("No data available")

        # 2.SHOW A CAR BASED ON INDEX(PRIMARY KEY)
        elif user_input == "2":
            if len(rental_cars) != 0:  # check if rental_car data exist
                car_id = get_user_input("Enter car ID: ", input_type=int)
                car_found = False  # Flag if car is found

                for car in rental_cars:
                    if car["car_id"] == car_id:
                        car_found = True
                        print("\t\t==== CHECK RENTAL CAR ====")
                        display_car_details([car])
                        break  # Exit the loop if the car is found

                if not car_found:
                    print("Car not found")
            else:
                print("No data available")

        # 3. RETURN TO MAIN MENU
        elif user_input == "3":
            return
        else:
            print("Invalid choice")


## CREATE RENTAL CAR
def create_car():
    while True:
        print("\t\t==== CREATE RENTAL CAR MENU ====")
        print(
            """
              1. Create new Rental Car
              2. Back to Menu
              """
        )
        user_input = input(" Please enter choice: ")

        if user_input == "1":
            print("==== Input Detail Mobil ====")
            while True:
                car_id = get_user_input("Enter car ID: ", input_type=int)
                car_exists = car_id in (car["car_id"] for car in rental_cars)

                if car_exists:
                    print(f"Data already exists for car ID: {car_id}")

                else:
                    car_brand = input("Enter car Brand: ")
                    car_model = input("Enter car Model: ")
                    while True:
                        try:
                            year = int(input("Enter car Year: "))
                            break  # Exit loop if the input is valid
                        except ValueError:
                            print("Please input the Year correctly.")

                    while True:
                        try:
                            rental_price = float(input("Enter Rental Price: "))
                            break
                        except ValueError:
                            print("Please input the price as number.")

                    while True:
                        # set input to lower & erase whitespace
                        availability_input = (
                            input("Enter availability (True/False): ").lower().strip()
                        )
                        if availability_input == "true":
                            availability = True
                            break
                        elif availability_input == "false":
                            availability = False
                            break
                        else:
                            print("Please input availability as True or False")
                    fuel_type = input("Enter Fuel Type: ")
                    transmission = input("Enter transmission type (Automatic/Manual): ")

                    new_car = {
                        "car_id": car_id,
                        "car_brand": car_brand,
                        "car_model": car_model,
                        "year": year,
                        "rental_price": rental_price,
                        "availability": availability,
                        "fuel_type": fuel_type,
                        "transmission": transmission,
                    }

                    # CONFIRMATION CREATE DATA
                    while True:
                        user_confirmation = confirmation_page()

                        if user_confirmation == "1":
                            rental_cars.append(new_car)
                            print("Data successfully saved")
                            show_list_of_cars()  # show new created car
                            break  # Exit loop
                        elif user_confirmation == "2":
                            break
                        else:
                            print("Invalid Choice")
                break

        elif user_input == "2":
            return
        else:
            print("Invalid choice")


## UPDATE RENTAL CAR
def update_car():
    while True:
        print("\t\t==== UPDATE RENTAL CAR MENU ====")
        print(
            """
                1. Update Rental Car
                2. Back to Menu
                """
        )
        user_input = input(" Please enter choice: ")

        if user_input == "1":
            car_id = get_user_input("Enter car ID: ", input_type=int)
            car_found = False

            for car in rental_cars:
                if car["car_id"] == car_id:
                    car_found = True

                    ## Display the rental car choosen
                    print("\t\t ==== RENTAL CAR ====")
                    display_car_details([car])

                    # CONFIRMATION UPDATE DATA
                    user_confirmation = confirmation_page()

                    while user_confirmation not in ["1", "2"]:
                        print("Invalid choice. Please enter 1 or 2.")
                        user_confirmation = confirmation_page()

                    if user_confirmation == "1":
                        while True:
                            print("==== CAR DETAIL PAGE ====")
                            print(
                                """ Pick a Column to change the data
                                1. Car brand
                                2. Car Model 
                                3. Year
                                4. Rental Price
                                5. Availability 
                                6. Fuel Type
                                7. Transmission
                                """
                            )

                            user_input = input("Enter your choice (1-7): ")

                            if user_input == "1":
                                car["car_brand"] = input("Enter updated car Brand: ")
                            elif user_input == "2":
                                car["car_model"] = input("Enter updated car Model: ")

                            elif user_input == "3":
                                while True:
                                    try:
                                        car["year"] = int(
                                            input("Enter updated car Year: ")
                                        )
                                        break  # Exit loop if the input is valid
                                    except ValueError:
                                        print("Please input the Year correctly.")

                            elif user_input == "4":
                                while True:
                                    try:
                                        car["rental_price"] = float(
                                            input("Enter Rental Price: ")
                                        )
                                        break
                                    except ValueError:
                                        print("Please input the price as a number.")

                            elif user_input == "5":
                                while True:
                                    availability_input = (
                                        input("Enter availability (True/False): ")
                                        .lower()
                                        .strip()
                                    )
                                    if availability_input == "true":
                                        car["availability"] = True
                                        break
                                    elif availability_input == "false":
                                        car["availability"] = False
                                        break
                                    else:
                                        print(
                                            "Please input availability as True or False"
                                        )

                            elif user_input == "6":
                                car["fuel_type"] = input(
                                    "Enter updated car Fuel Type: "
                                )
                            elif user_input == "7":
                                car["transmission"] = input(
                                    "Enter updated car Transmission (Automatic/Manual): "
                                )
                            else:
                                print("invalid choice")
                                continue

                            print("Data successfully updated")
                            break

                    elif user_confirmation == "2":
                        break
                    else:
                        print("Invalid Choice")

            if not car_found:
                print("The data you are looking for does not exist")

        elif user_input == "2":
            return

        else:
            print("Invalid Choice")


## DELETE CAR
def delete_car():
    while True:
        print("==== DELETE RENTAL CAR MENU ====")
        print(
            """
              1. Delete Rental Car
              2. Back to Menu
              """
        )
        user_input = input("Enter choice: ")

        if user_input == "1":
            # Check if data exists or not
            if len(rental_cars) != 0:
                show_list_of_cars()

                delete_car_id = get_user_input(
                    "Enter car index to Delete: ", input_type=int
                )
                car_found = False

                for car in rental_cars:
                    if car["car_id"] == delete_car_id:
                        car_found = True

                        # CONFIRMATION DELETE DATA
                        user_confirmation = confirmation_page()

                        while user_confirmation not in ["1", "2"]:
                            print("Invalid choice. Please enter 1 or 2.")
                            user_confirmation = confirmation_page()

                        if user_confirmation == "1":
                            rental_cars.remove(car)
                            print("\n\nCar successfully deleted")
                            show_list_of_cars()  # Show the updated list of cars
                            break

                if not car_found:
                    print("The data you are looking for does not exist")
                break  # Exit the loop if the car is found or not found

            else:
                print("No cars to delete.")

        elif user_input == "2":
            return
        else:
            print("Invalid choice")


## OTHER FEATURES
def others_menu():
    while True:
        print("\t\t==== Others Menu ====")
        print(
            """ 
                1. Sort Cars
                2. Car Maintenance
                3. Back to Menu
            """
        )
        user_input = input("Enter your choice: ")
        if user_input == "1":
            sorting()
        elif user_input == "2":
            maintenance_menu()
        elif user_input == "3":
            return
        else:
            print("Invalid choice")


## MAIN MENU
def main_menu():
    while True:
        print("\n\t======== WELCOME TO RENTAL CAR MENU ========")
        print(
            """ List Menu:
              1. Show Rental Car List
              2. Create Rental Car
              3. Update Rental Car
              4. Delete Rental Car
              5. Others...
              6. Exit
              """
        )
        user_input = input("Enter your choice: ")
        if user_input == "1":
            show_cars()
        elif user_input == "2":
            create_car()
        elif user_input == "3":
            update_car()
        elif user_input == "4":
            delete_car()
        elif user_input == "5":
            others_menu()
        elif user_input == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()
