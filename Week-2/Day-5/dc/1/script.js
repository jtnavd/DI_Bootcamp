var num = 99;
var subNum = 1;

do {
    newNum = num - subNum;
    console.log(num+" bottles of beer on the wall.");
    console.log(num+" bottles of beer.");
    console.log("Take "+ subNum+ " down, pass it around");
    num-subNum;
    subNum++;
console.log(newNum + " bottles of beer Left on the wall.");}
while (num > subNum);

// function checkBottle(num) {
//     if (num <=0){
//         console.log("There's no bottle left on the wall.");

//     }
// }