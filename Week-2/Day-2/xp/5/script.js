let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

let NumberUsers=+prompt("How many users ?")
let GetNum= users.length

switch (users){
    case"Lea123":
        console.log("Lea123")
    break;
    case"Princess45":
        console.log("Princess45")
    break;
    case"cat&doglovers":
        console.log("cat&doglovers")   
    break;
    case"helooo@000":
        console.log("helooo@000")
    break;
    default:
        NumberUsers ===0
        console.log("no one is online")
}

if (NumberUsers >= 1){
 console.log(GetNum+"is Online")   
}


// Using the array above, console.log the number of users in a group chat based on the following rules:
// If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
// For example, if there are 5 users, it should display: