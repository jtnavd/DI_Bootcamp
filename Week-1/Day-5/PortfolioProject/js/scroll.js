// $(document).ready(function() {
//     $(".fa-bars").click(function(){
//         $(this).toggleClass('fa-times');
//         $('.navbar').toggleClass('nav-toggle');
//     });

//     $(window).on('scroll load',function(){
//         if($(window).scrollTop() <25){
//             $('.header').hide();
//         }
//         else{
//             $('.header').show();
//         }
//     })
// })

//NAVBAR SCROLLING #################################################################
var prevscrollpos = window.pageYOffset;
window.onscroll= function(scrolling){

    var currentscrollpos = window.pageYOffset;
    if (prevscrollpos > currentscrollpos){
        document.getElementById("navbar").style.top = "0";
    }
    else {
        document.getElementById("navbar").style.top = "-80px"
    }
    prevscrollpos = currentscrollpos;
}