
plan = {}

def plan_day():

    arrivals = []
    departures = []

    day = int(input("Enter Day You Want To Plan for ( 1 -30 ): "))

    if day > 0 and day < 30:
    
        arr_flight = int(input(f"How Many flights are arriving on day {day}: "))
        
        for i in range (arr_flight):
            flt_detail = input("Enter Flight Number: ")
            arrivals.append(flt_detail)
        
        depart_flight = int(input(f"How Many flights are Departing on day {day}: "))
        
        for i in range (depart_flight):
            flt_detail = input("Enter Flight Number: ")
            departures.append(flt_detail)

        runway = int(input(f"What Runway will be Used on Day {day}: "))
        weather = int(input(f"How is the Weather on Day {day} ?\n1. Clear\n2. Windy\n3. Cloudy\nYour Choice: "))
        match weather:
            case 1:
                weather = "Clear"
            case 2:
                weather = "Windy"
            case 3:
                weather = "Cloudy"

        maintenance = input(f"Is There Some Maintenance Planned For Day {day}? (yes/no): ").upper()
            
        plan[day]={
            "arrival": arrivals,
            "departure": departures,
            "runway": runway,
            "weather": weather,
            "maintenance": maintenance
            }
    else:
        print("Not A Valid Input !!! ")

def flight_print():
    chose = int(input("Enter Day # to Print: "))

    if chose > 0 and chose < 30:

        data = plan[chose]
        print(f"==========\n  Day {chose}:\n==========\nArrival Flights: {data['arrival']}\nDeparture Flights: {data['departure']}\nRunway: {data['runway']}\nWeather: {data['weather']}\nMaintenance: {data['maintenance']}")
    else: 
        print("Not a Valid Day !!! ")

def search_flight():
    flight_no = input("Enter Flight Number: ")

    found = False

    for day, data in plan.items():

        if flight_no in data["arrival"]:
            print(f"Flight Found!")
            print(f"Day: {day}")
            print("Type: Arrival")
            found = True

        elif flight_no in data["departure"]:
            print(f"Flight Found!")
            print(f"Day: {day}")
            print("Type: Departure")
            found = True

    if not found:
        print("Flight not found.")

def print_summary():
    if not plan:
        print("No data available.")
        return

    print("\n--- Airport 30-Day Summary ---\n")

    for day, info in plan.items():
        total_arrivals = len(info['arrival'])
        total_departures = len(info['departure'])
        print(f"Day {day}: Arriving Flights = {total_arrivals}, Departing Flights = {total_departures}")

while True:
    print("Welcome to SkyPlan !\n' A 30 Day Flight Operations Planner '")
    choice = int(input("1. Plan A Day\n2. Show Day Info\n3. Search For A Flight\n4. Print Planner Summary\n5. Exit System\nYour Choice: "))
    
    match choice:
        case 1:
            plan_day()
        case 2:
            flight_print()
        case 3:
            search_flight()
        case 4:
            print_summary()
        case 5:
            print("Exiting SkyPlan. Goodbye!")
            break
        case _:
            print("Invalid Input !! ")