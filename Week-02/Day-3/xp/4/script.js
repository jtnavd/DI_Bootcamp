// EXERCISE 4

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

guestChoice= prompt("Write student name");

  if(guestList[guestChoice]){
    console.log("Hi! I'm ",guestChoice, ", and I'm from ", guestList[guestChoice]);
  }
  else{console.log("Hi, I'm a guest.")}