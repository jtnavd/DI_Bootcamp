function playSound(e){
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`key[data-key="${e.keyCode}"]`);
    if(!audio)return;
    audio.currentTime = 0;
    audio.play();
    key.classList.add('playing');
}
function removeTransit(e){
     if(e.propertyName === 'transition')return;
}
const keys = document.querySelectorAll('.key');
keys.forEach(key=>key.addEventListener('transitionend', removeTransit));
window.addEventListener('keydown', playSound);