computerNumber = Math.floor(Math.random() *11);
console.log("Number" + computerNumber)

function  playTheGame(){
    
    if (confirm(true)){
            userNumber = +prompt("Choose a number between 1 and 10")
            if (userNumber.isInteger){
                if(userNumber>0 && userNumber<10){

                }
                else{
                    alert("Sorry it’s not a good number, Goodbye");
                }
            }
            else{
                	alert("Sorry Not a number, Goodbye");
            }
    }
    else{
        alert("No problem, Goodbye!");
    }
}


playTheGame



// In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).

// If his answer is true, follow these steps:
// Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :

// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.
