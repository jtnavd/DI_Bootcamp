let language = prompt("What language are you speaking")
Conv1=language.toLowerCase


switch(Conv1){
    case "french":
        answer = "Bonjour";
        break;
    case "english":
        answer = "Hello";
        break;
    case "hebrew":
        answer = "Shalom";
        break;
}

if(language == Conv1){
    console.log(answer);
}

else{console.log("01110011 01101111 01110010 01110010 01111001");}