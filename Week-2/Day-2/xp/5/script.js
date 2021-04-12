let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

let NumberUsers=+prompt("How many users ?")
let GetNum= users.length

if(users===0){
    console.log("no one is online")
}

else if (NumberUsers === 1){
    console.log(users[0]," is Online")   
}
else if (NumberUsers === 2){
    console.log(users[0] ,", "+ users[1]," is Online")   
}
else if (NumberUsers === 3){
    console.log(users[0] ,", "+ users[1],", "+ users[2]," is Online")  
} 

else{
    console.log(users, "Is online")
}