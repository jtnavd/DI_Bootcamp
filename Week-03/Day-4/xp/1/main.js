function myMove(){
    var container = document.getElementById('container');
    var el = document.getElementById('animate');
    var id = setInterval(frame, 5);
    var maxDistance = container.offsetWidth - el.offsetWidth;
    var pos = 0;
    var end = maxDistance;
    var dir = 1;

    function frame(){
        if (pos == end){
        dir *= -1;
        end = Math.abs(maxDistance - end);
    }
    pos += dir;
    el.style.left = pos + 'px';
    // console.log(frame);
}
}