class TravelPlanner:
    def __init__(self):
        self.destinations = []
        self.itinerary = {}
    
    def add_destination(self):
        destination = input("\nEnter your travel destination: ")
        days = int(input(f"How many days do you plan to stay in {destination}? "))
        
        accommodation = input(f"Where will you stay in {destination} (Hotel, Airbnb, etc.)? ")
        transport = input(f"How will you travel to {destination} (Flight, Train, Bus, etc.)? ")
        
        budget = self.get_budget_details()

        activities = []
        for day in range(1, days + 1):
            print(f"\nDay {day}:")
            daily_activities = []
            while True:
                activity = input(f"Enter an activity for Day {day} (or type 'done' to finish): ")
                if activity.lower() == 'done':
                    break
                daily_activities.append(activity)
            activities.append(daily_activities)

        self.destinations.append(destination)
        self.itinerary[destination] = {
            'days': days, 
            'accommodation': accommodation, 
            'transport': transport, 
            'activities': activities, 
            'budget': budget
        }

    def get_budget_details(self):
        print("\nEnter your estimated budget details:")
        accommodation_cost = float(input("Estimated accommodation cost per day: $"))
        food_cost = float(input("Estimated food cost per day: $"))
        activity_cost = float(input("Estimated cost of activities per day: $"))
        transport_cost = float(input("Estimated transport cost for the whole trip: $"))
        
        total_budget = (accommodation_cost + food_cost + activity_cost) * 7  # assuming 7 days by default for calculation
        total_budget += transport_cost
        return {
            'accommodation': accommodation_cost,
            'food': food_cost,
            'activities': activity_cost,
            'transport': transport_cost,
            'total_budget': total_budget
        }

    def view_itinerary(self):
        print("\nYour Travel Itinerary:")
        for destination, details in self.itinerary.items():
            print(f"\nDestination: {destination}")
            print(f"Number of days: {details['days']}")
            print(f"Accommodation: {details['accommodation']}")
            print(f"Transport: {details['transport']}")
            print("Planned activities:")
            for day, daily_activities in enumerate(details['activities'], 1):
                print(f"  Day {day}:")
                for activity in daily_activities:
                    print(f"    - {activity}")
            print("\nBudget Breakdown:")
            print(f"Accommodation cost per day: ${details['budget']['accommodation']}")
            print(f"Food cost per day: ${details['budget']['food']}")
            print(f"Activity cost per day: ${details['budget']['activities']}")
            print(f"Transport cost: ${details['budget']['transport']}")
            print(f"Total estimated budget: ${details['budget']['total_budget']}")

    def run(self):
        while True:
            print("\nGlobeTrekker Menu:")
            print("1. Add a destination")
            print("2. View itinerary")
            print("3. Exit")
            choice = input("Please choose an option (1/2/3): ")

            if choice == '1':
                self.add_destination()
            elif choice == '2':
                self.view_itinerary()
            elif choice == '3':
                print("Thank you for using GlobeTrekker!")
                break
            else:
                print("Invalid choice. Please select again.")


# Running the travel planner
if __name__ == "__main__":
    planner = TravelPlanner()
    planner.run()
