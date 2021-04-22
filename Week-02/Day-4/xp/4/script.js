let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
// Create a function called checkBasket().
// It should:
// prompt the user for an item
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional

function checkBasket(itemName, amazonBasket) {
    user= prompt("Which item are you looking for?");
    if(itemName=["glass","glasses","book","books","floss"]){
       console.log(Object.keys(amazonBasket));

    }
    else{console.log("Sorry, we don't have this sort of item");}
}



checkBasket();