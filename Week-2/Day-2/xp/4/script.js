let whatHappens;

let direction = prompt(" chose forward, back, left, right")

switch (direction) {
    case "forward":
        whatHappens = "you encounter a monster";
        break;
    case "back":
        whatHappens = "you arrived home";
        break;
    case "right":
        whatHappens = "you found a river";
        break;
    case "left":
        whatHappens = "you run into a troll";
        break;
    default:
        console.log("please enter a valid direction");
}

console.log(whatHappens);
