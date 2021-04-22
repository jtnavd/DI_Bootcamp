const container = document.querySelector('.container')
const btnrgb = document.querySelector('.button')

function creatDivs(col , rows) {
    for(let i = 0;i < (col * rows); i++) {
        const div = document.createElement('div') 
        div.style.border= '0.5px solid black';
        div.style.width= '20px';
        div.style.height= '20px';
        container.style.maxheight= 100;
        // container.style.maxWidth=100;
        container.style.gridTemplateColumns = `repeat(${col}, 1fr)`;
        container.style.gridTemplateRows = `repeat(${rows}, 1fr)`;
        container.appendChild(div).classList.add('box')
    }
}

creatDivs(16,16)

// function blackColor(){
//     const boxs = container.querySelectorAll('.box');
//     btnblack = document.createAttribute("color")
//     btnblack.textContent = 'Black';
//     btnblack.addEventListener('click', ()=>{
//         boxs.forEach(box=>box.addEventListener('mouseover', ()=>{
//             boxs.style.background = "black";
//         })) 
//     })

//     buttonContainer.appendChild(btnblack).classList.add('btn')
// }