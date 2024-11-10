# Define the Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile subclass, inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Initialize the vehicle_type attribute from Vehicle
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function to get automobile information from the user
def get_automobile_info():
    # Set the vehicle type to "car" for this application
    vehicle_type = "car"
    
    # Get user input for other attributes
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an Automobile object with the collected information
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Display the information in a formatted output
    print("\nHere is the information about your car:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

# Run the application
get_automobile_info()
