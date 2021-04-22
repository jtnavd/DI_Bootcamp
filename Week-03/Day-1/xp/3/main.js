let changeTitle = document.querySelector('div').style.background = 'lightblue';
changeTitle.display='block';
changeTitle.padding="50px 10px 20px 30px";

let removeName = document.getElementsByTagName("li")[0].remove("John");
let addBorder = document.getElementsByName("Pete").style.border = "10px solid black";

document.body.style.fontSize = '60px';
console.log(addBorder);



// Add a border to the second name (Pete).
// Bonus: If the background color of the div is “light blue”., alert “Hello x and y” (x and y are the users in the div).