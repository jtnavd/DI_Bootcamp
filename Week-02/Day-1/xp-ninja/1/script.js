let sentence1="I can't find Nemo.";
let sentence2="I found .";
let sentence3="Dori's best firend is ";


let searchWord = " " + "Nemo" + " ";
//SENTENCE 2 INTEGRATION
var position1 = 7;
var output1=sentence2.slice(0,position1).join(searchWord);

//SENTENCE 3 INTEGRATION
var position2 =21;
var output=[sentence3.slice(0,position2),sentence3].join(searchWord);

//RESULT
console.log(sentence1);
console.log(output1);
console.log(output2);
