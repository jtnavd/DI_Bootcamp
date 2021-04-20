let libButton = document.getElementById('lib-button');


function madLibs(){
var storyDiv = document.getElementById('story');
var noun = document.getElementById('noun').value;
var adjective = document.getElementById('Adjective').value;
var someName = document.getElementById('person').value;
var Verb = document.getElementById('verb').value;
var Aplace = document.getElementById('place').value;


// for (let i of document.getElementsByTagName('input')){
//     if(i.value.lenght === 0){
//         i.style.color ='red';
//         abort = true;
//         // console.log("is empty")
//     }
//     else{
//         i.style.color ='none';
//     }
// };
// if (abort){return;};


storyDiv.innerHTML = "I took my "+ noun + " and "+adjective+" it "+Verb+" to "+someName+ " in "+Aplace;

// let unit = document.createElement('p')
// unit.innerText=storyDiv;
// document.getElementById('story').appendChild(unit);
};
libButton.addEventListener('click', madLibs);


// Get the value of each of the inputs in the HTML file when the button is clicked. INDEX _ VALUE
// Make sure the values are not empty      CONDITION
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the g