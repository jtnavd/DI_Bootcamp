// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01

let values = [0.25,0.10,0.05,0.01]    
function changeEnough(change, itemCost){
    let sum = 0;
    for (let i = 0; i < change.length; i++) {
        let amount = change[i] * values[i];
        sum += amount;
    }
    if (sum>itemCost){console.log(true,"You have enough money in your wallet")}
    else{console.log(false,"Sorry, You don't have enough money in your wallet")}
}

changeEnough([2, 100, 0, 0], 14.11);
changeEnough([0, 0, 20, 5], 0.75);
changeEnough([2, 6, 0, 0], 50.00);
changeEnough([2, 50, 0, 0], 100.00);

