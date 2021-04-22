let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}

console.log("number of levels in building : ",building.number_levels);
console.log("number of appartments in 4th level : ",building.number_of_apt_by_level["4"]);


// Console.log the number of levels in the building.
// Console.log how many apartments are on levels 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent.
// If it is than increase Dan’s rent.