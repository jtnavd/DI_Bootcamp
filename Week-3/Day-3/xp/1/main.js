//REMOVE LAST PARAGRAPH
let removeP = document.getElementsByTagName("p")[3];
removeP.remove();
//CHANGE H2 BACKGROUND COLOR ON CLICK
let h2bg = document.querySelector("h2");
h2bg.addEventListener("click", function changeColor() {
    h2bg.style.backgroundColor = 'yellow';
});
//RANDOM FONT SIZE
let h1fs = document.getElementsByTagName("h1")[0];
h1fs.addEventListener("click", function (){
    h1fs.style.fontSize =`${Math.random()* 101}px`;
});
// HIDE/SHOW H3
let hideShow = document.getElementsByTagName("h3");
 function changeBold(){
    hideShow.style.display = 'none';
};
// //BOLD PARAGRAPH 
let boldParagraph = document.getElementsByClassName('switchBTN');
boldParagraph.addEventListener('click', function(){
    document.getElementsByTagName('p').style.fontSize='300px';
    console.log('hide')
});
// Add an event listener which will hide the h3 when it’s clicked on (use the display property).            X
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold. X
// When the “Submit” button of the form is clicked:                                                         
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
// When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
