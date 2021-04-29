# def describe_city(city = 'Brussels' ,country= 'Belgium'):
#     return print{city + ' is in '+ country}
    
# describe_city()

# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country):
    return f'{city},{country}'

print(describe_city("Anvers","Belgium"))

print(describe_city("brussels", "Belgium"))