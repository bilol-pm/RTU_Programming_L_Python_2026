"""
Lab 2.1 – Simple Datasets and Aggregates
----------------------------------------
Practice lists, dictionaries and tuples by computing simple aggregates.

Write these functions:
- average(values)               -> float
    Average of a list of numbers. Return 0.0 if the list is empty.
- largest_city(populations)     -> tuple (name, population)
    The city with the LARGEST population.
- smallest_city(populations)    -> tuple (name, population)
    The city with the SMALLEST population.
- total_population(populations) -> int
    Sum of all populations. Return 0 if the dict is empty.

`populations` is a dictionary like {"Riga": 605000, "Daugavpils": 78000}.
For largest_city() and smallest_city():
- If two cities tie, return the one that comes FIRST in the dictionary.
- If the dictionary is empty, return ("", 0).
- Built-ins such as sum(), len(), max() and min() are allowed.
  Hint: max(populations, key=populations.get) gives the key with the
  largest value.

In the main block: create your OWN datasets (a list `temperatures` with
7 daily temperatures, and a dict `city_population` with at least 5 cities),
call the functions, and print the results. Print the average with
1 decimal place.

Example run (with your own data the numbers will differ):
    Average temperature: 4.3
    Largest city: Riga - 605000
    Smallest city: Valmiera - 23000
    Total population: 806000

Examples (these are also used to check your work):
>>> average([1, 2, 3, 4])
2.5
>>> average([])
0.0
>>> cities = {"Riga": 605000, "Daugavpils": 78000, "Liepaja": 67000}
>>> largest_city(cities)
('Riga', 605000)
>>> smallest_city(cities)
('Liepaja', 67000)
>>> total_population(cities)
750000
>>> largest_city({})
('', 0)
>>> largest_city({"A": 10, "B": 10})
('A', 10)
"""


def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    # TODO: implement
    if not values:
        return 0.0
    sum_of_numbers = 0
    for value in values:
        sum_of_numbers += value
    return sum_of_numbers / len(values)



def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    max_city = ""
    max_pop = -1
    for city, population in populations.items():
        if population > max_pop:
            max_pop = population
            max_city = city
    return (max_city, max_pop)


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    min_city = list(populations.keys())[0]
    min_pop = populations[min_city]

    for city, population in populations.items():
        if population < min_pop:
            min_pop = population
            min_city = city

    return (min_city, min_pop)


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    if not populations:
        return 0
    return sum(populations.values())


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.

    # 1. Ask the user to input 7 daily temperatures
    print("Please enter 7 daily temperatures:")
    temperatures = []
    for i in range(1, 8):
        temp = float(input(f"Temperature for day {i}: "))
        temperatures.append(temp)

    # 2. Ask the user to input cities and their populations
    print("\nEnter cities and populations (type 'stop' as the city name to finish):")
    city_population = {}
    while True:
        city_name = input("City name: ").strip()
        if city_name.lower() == "stop":
            break
        population = int(input(f"Population of {city_name}: "))
        city_population[city_name] = population

    # 3. Call functions and display the results
    print("\n--- RESULTS ---")
    avg_temp = average(temperatures)
    print(f"Average temperature: {avg_temp:.1f}")

    if city_population:
        largest = largest_city(city_population)
        smallest = smallest_city(city_population)
        total_pop = total_population(city_population)

        print(f"Largest city: {largest[0]} - {largest[1]}")
        print(f"Smallest city: {smallest[0]} - {smallest[1]}")
        print(f"Total population: {total_pop}")
    else:
        print("No cities were entered!")
