let values = {
    fname: '',
    lname: ''
}

let input = document.getElementsByTagName("input");

for (input in inputs){
    input.addEventListener('change', function(e){
        value = {
        ...values,
            [e.target.name]:e.target.value
        }
        console.log(values);
        })
} 
let form = document.getElementsByTagName('form')[0];

form.addEventListener('submit',function(e){
        e.preventDefault();
        alert(`Welcome ${values.fname} ${values.lname}`)
})