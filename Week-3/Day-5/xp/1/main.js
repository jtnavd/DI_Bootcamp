const container = document.querySelector('container')
const btnblack = document.querySelector('button')
const btnrgb = document.querySelector('button')
const btnsize = document.querySelector('button')
const buttonContainer = document.querySelector('button')

function creatDivs(col , rows) {
    for(let i = 0;i < (col * rows); i++) {
        const div = document.createElement('div') 
        container.style.gridTemplateColumns = `repeat(${col}, 1fr)`;
        container.style.gridTemplateRows = `repeat(${rows}, 1fr)`;
        container.appendChild(div).classList.add('box')
    }
}

creatDivs(16,16)

function blackColor(){
    const boxs = container.querySelectorAll('.box')
    btnblack.textContent = 'Black';
    btnblack.addEventListener('click', ()=>{
        boxs.forEach(box=>box.addEventListener('mouseover', ()=>{
            boxs.style.background = "black";
        })) 
    })

    buttonContainer.appendChild(btnblack).classList.add('btn')
}