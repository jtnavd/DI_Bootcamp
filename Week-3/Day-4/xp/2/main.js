function onDragStart(event) {
    event.dataTransfer.setData('text/plain',event.target.id);
    event.currentTarget.style.backgroundColor ='yellow';
    console.log("DRAG")
}
function onDragOver(event) {
    event.preventDefault();
    console.log('OVER');
}
function onDrop(event) {
    console.log('DROP');
    const id = event.dataTransfer.getData('text');
    const dragElement = document.getElementById(id);
    const drop = event.target;
    drop.appendChild(dragElement);
    event.dataTransfer.clearData();
}