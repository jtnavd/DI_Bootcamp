const input = document.querySelector('#add');
const btn = document.querySelector('#btn');
const list = document.querySelector('#list');
var el = document.getElementsByTagName('li');

btn.onclick = function{
    var text = input.value;
    if(txt == ''){
        alert('Write something please');
    }
    else{
        li = document.createElement('li');
        li.innerHTML = txt;
        list.insertBefore(li,list.childNodes[0]);
        input.value = '';
    }
}

// btn.addEventListener('click', ()=>{
//     let txt=input.value;
//     if(txt===""){
//         alert('Add a task please');
//     }
//     else{
//         let li=document.createElement('li');
//         li.innerHTML = txt;
//         list.insertBefore(li, list.childNodes[0]);
//         input.value='';
//     }
// })

list.onclick = function(e){
    if(e.target.tagName == 'LI'){
         e.target.classList.toggle('checked');
    }
};

// list.addEventListener('click', e=>{
//     if(e.target.tagname == 'LI'){
//         e.target.classList.toggle('checked');
//     }
// })