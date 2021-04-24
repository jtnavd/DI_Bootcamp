let str1=""

function Aletter(){
    for (let i = 0; i < 7; i++) {
        for (let i = 0; i < 5; i++) { 
           if (((col==0 || col==4) && row!=0) || ((row==0 || row==3) && (col>0 && col<4))){
               str1 = str1+"*"
           }
           else{
            str1 = str1+" "
           }  
        }  
    }
}


console.log()
