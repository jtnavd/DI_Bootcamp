let verb= prompt("Enter a verb please!");
let str1= "ing";
let str2= "ly";

if(verb.length > 3){
    if(str1.indexOf(verb)){
        verb+=str2;
        console.log(verb);
    }
    else{
        verb+=str1;
        console.log(verb);
    }
}