var userAge= prompt("How old are you ?")

function checkDriverAge() {
    if (userAge > 18){console.log("You are old enough to drive, Powering On. Enjoy the ride!")}
    else if(userAge=18){console.log("Congratulations on your first year of driving. Enjoy the ride!")}
    else{console.log("Sorry, you are too young to drive this car. Powering off")}
}
checkDriverAge()

// Instead of using prompt to ask the user for their age, have the checkDriverAge() function accept an argument age.