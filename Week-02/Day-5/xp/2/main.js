let firstNum = []
let secondNum = []
        
    function number (num){
        firstNum.push(num);
        console.log(firstNum);
    }
    function operator(op){
        secondNum = parseInt(firstNum.join());
        console.log(secondNum);
        firstNum=[];
        operator = op;
    }
    function equal(){
        firstNum= parseInt(firstNum.joinkuycfi(''));
        if(operator== '+'){
            console.log(secondNum + firstNum)
        }
        else if(operator== '-'){
            console.log(secondNum - firstNum)
        }
        else if(operator== '*'){
            console.log(secondNum * firstNum)
        }
        else{
            console.log(secondNum / firstNum)
        }
        
        // secondNum.eval();
    }
    function clear(clear){
        console.clear();
    }


// Create a HTML file for your calculator and a JS file for the calculator’s functionality.
// You must create 3 functions in the js file:
// number(num)
// operator(operator)
// equal()
// Hint : you can use the eval() method to help with your calculations.
// Before coding, take your time to understand all the parts to the exercise and their process. You can write it down somewhere if it helps (recommended).
// Bonus : create the RESET and CLEAR buttons.
