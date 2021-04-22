
function getBold() {
    let bold = document.getElementsByTagName('strong');
return bold;
}

function paintIt(color) {
    let arr = getBold();
    for (let i of arr){
        i.style.color =color;
    }
}


function highlight(){
paintIt('blue');
console.log("blueeeee")
}
function returnColor(){
paintIt('black')
}

let par = document.querySelector('p');
par.addEventListener("mouseover", highlight);
par.addEventListener("mouseout", returnColor);
console.log (paintIt)
