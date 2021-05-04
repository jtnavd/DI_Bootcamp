brand = {
    'name': 'Zara' ,
    'creation_date': '1975',
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ('men', 'women', 'children', 'home'), 
    'international_competitors': ('Gap', 'H&M', 'Benetton'),
    'number_stores': '7000' ,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ('pink', 'green')
    }
}

brand.update({'number_stores':'2'})

print(brand)

brand["number_stores"] = 2

print("\nZara clients : {}, also visit {}".format(', '.join(brand["type_of_clothes"]), ', '.join(brand["international_competitors"])))

# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details: