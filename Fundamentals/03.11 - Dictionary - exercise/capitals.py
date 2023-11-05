# Using a dictionary comprehension, write a program that receives country names on the first line,
#   separated by comma and space ", ", and their corresponding capital cities on the second line
#   (again separated by comma and space ", "). Print each country with their capital
#   on a separate line in the following format: "{country} -> {capital}".
# Hints
# You could use the zip() method.

country_names = [x for x in input().split(", ")]
capital_names = [x for x in input().split(", ")]
capital_cities = dict(zip(country_names, capital_names))
for country, capital in capital_cities.items():
    print(f"{country} -> {capital}")
