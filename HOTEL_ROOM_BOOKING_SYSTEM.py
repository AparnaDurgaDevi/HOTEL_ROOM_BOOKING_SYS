def show_rooms():
    print("\n----- ROOM TYPES -----")
    print("1. Single Room - Rs.1500/day")
    print("2. Double Room - Rs.2500/day")
    print("3. Deluxe Room - Rs.4000/day")


def select_room():
    room_type = int(input("Enter Room Type: "))

    if room_type == 1:
        room_name = "Single Room"
        price = 1500

    elif room_type == 2:
        room_name = "Double Room"
        price = 2500

    elif room_type == 3:
        room_name = "Deluxe Room"
        price = 4000

    else:
        room_name = "Invalid Room"
        price = 0

    return room_name, price


def calculate_room_cost(price, days):
    return price * days


def calculate_service_charge():
    return 500


def calculate_discount(room_cost, days):

    if days >= 5:
        discount = room_cost * 0.10

    elif days >= 3:
        discount = 1000

    else:
        discount = 0

    return discount


def generate_bill(room_name, price, days, room_cost,
                  service_charge, discount):

    final_amount = room_cost + service_charge - discount

    print("\n===== HOTEL BOOKING BILL =====")
    print("Room Type      :", room_name)
    print("Price per Day  : Rs.", price)
    print("Number of Days :", days)
    print("Room Cost      : Rs.", room_cost)
    print("Service Charge : Rs.", service_charge)
    print("Discount       : Rs.", discount)
    print("-------------------------------")
    print("Final Amount   : Rs.", final_amount)
    print("-------------------------------")
    print("Thank you for booking with us!")


# Main Program

print("===== HOTEL ROOM BOOKING SYSTEM =====")

show_rooms()

room_name, price = select_room()

if price == 0:
    print("Invalid room selection.")

else:
    days = int(input("Enter Number of Days: "))

    if days <= 0:
        print("Number of days must be greater than 0.")

    else:
        room_cost = calculate_room_cost(price, days)

        service_charge = calculate_service_charge()

        discount = calculate_discount(room_cost, days)

        generate_bill(
            room_name,
            price,
            days,
            room_cost,
            service_charge,
            discount
        )