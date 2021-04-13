// EXERCISE 6

let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  for (let property in details) {
    console.log(property," ", details[property]);      
  }