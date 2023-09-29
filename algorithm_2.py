#Team 6: Aria Askaryar, Shriya Bannikop
"""
Algorithm 2: Unique Starting City

You have a series of cities arranged in a circle, each with its own gas 
station. Given the distances between the cities and the mileage your car
 gets per gallon of fuel, you need to determine which city to start from 
 so that you can complete a full circle back to the starting city, 
 refueling at each city along the way, and ending with 0 or more gallons 
 of fuel left. This optimal city is termed the "preferred starting city," 
 and there is always one such city in the given problem.

Functions:
    - unique_starting_city: identifies a unique city from which one can start a circular tour, given the fuel availability, distances between cities, and the mileage of the vehicle.
    
Usage example:
    city_distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    result = unique_starting_city(city_distances, fuel, mpg)
"""

# Function to find the unique starting city for a circular tour
def unique_starting_city(city_distances, fuel, mpg):
    # Initialize variables
    start = 0            # Starting city
    required_fuel = 0    # (will be negative mostly) this variable is to store the fuel that was required to travel to the  next city i.e the amount of fuel that was needed
    extra_fuel = 0       # Extra fuel left after travelling from one city to next
    n = len(fuel)        # to get the number of cities

  # Iterate through each city
    for i in range(n):
       # Calculate extra fuel at the current city
        extra_fuel += (fuel[i] * mpg - city_distances[i])
      
      # If extra fuel is negative then the person cannot travel to next city, so update the starting city and required fuel
        if extra_fuel < 0:
          #update the starting city to next city as going through the pervious cities will give negative fuel and iterating though those cities again will increase complexity
            start = i + 1
          #we will not have to travel through these cities again as the calculated fuel is already stored in required fuel
            required_fuel += extra_fuel
            extra_fuel = 0

  # Check if there is enough total fuel (requiredFuel + extraFuel) to complete the circular tour
    if required_fuel + extra_fuel >= 0:
        return start # Starting city index
    else:
        return -1 # Circular tour is not possible, so there is no starting city

# Define the input values
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Call the function with the provided inputs
result = unique_starting_city(city_distances, fuel, mpg)

if result != -1:
//will print the index of the unique starting city
    print(f"{result}")
else:
  //will print if 
    print("No circular tour is possible.")
