def cost_of_trip(city, return_flight, hotel_cost, car_rental):
    duration = 0
    trip_cost = return_flight + (hotel_cost + car_rental / 7) * duration
    while trip_cost <= budget:
        duration += 1
        trip_cost = return_flight + (hotel_cost + car_rental / 7) * duration

    trip_cost = return_flight + (hotel_cost + car_rental / 7) * (duration - 1)
    print("The cost for trip at the city of {} is".format(city), round(trip_cost), "and the number of day is",
          duration - 1, "days.")

    return cost_of_trip

def cost_of_trip_rag(city, return_flight, hotel_cost, car_rental):

    trip_cost = (hotel_cost + car_rental / 7)
    greatest_divisor = int((budget-return_flight) / trip_cost)
    total_cost = (trip_cost * greatest_divisor) + return_flight

    print("The cost for trip at the city of {} is".format(city), round(total_cost), "and the number of day is",
          greatest_divisor, "days.")

    return total_cost


budget = float(input("Enter your budget in $"))

Paris = cost_of_trip(
    city="Paris",
    return_flight=200,
    hotel_cost=20,
    car_rental=200,
)

London = cost_of_trip(
    city="London",
    return_flight=250,
    hotel_cost=30,
    car_rental=120,
)
Dubai = cost_of_trip(
    city="Dubai",
    return_flight=370,
    hotel_cost=15,
    car_rental=80,
)
Mumbai = cost_of_trip(
    city="Mumbai",
    return_flight=450,
    hotel_cost=10,
    car_rental=70,
)

cost_of_trip_rag(
    city="Paris",
    return_flight=200,
    hotel_cost=20,
    car_rental=200,
)

cost_of_trip_rag(
    city="London",
    return_flight=250,
    hotel_cost=30,
    car_rental=120,
)
cost_of_trip_rag(
    city="Dubai",
    return_flight=370,
    hotel_cost=15,
    car_rental=80,
)
cost_of_trip_rag(
    city="Mumbai",
    return_flight=450,
    hotel_cost=10,
    car_rental=70,
)