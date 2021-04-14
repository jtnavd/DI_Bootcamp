function parentsAge(){
    // myAge= prompt ("How old are you?");
    let momAge= myAge*2;
    let dadAge= momAge*1.2;
    console.log("You are : " + myAge,
     "Your mother is : " + momAge,
      "Your father is : " +dadAge.toFixed());
};

parentsAge(23);