document.getElementById('navBar').setAttribute("id",'socialNetworkNavigation');    

function addToList() {
    var addElement = document.createElement('li');
    var a = document.createElement('a');
    a.innerHTML = 'Logout';
    a.setAttribute('class');
    a.className('#');
    addElement.appendChild(a);
    // var listElement1 = document.createTextNode('Logout');
    addElement.appendChild(listElement1);
    let ul = document.getElementsByTagName('ul')[0];
    ul.appendChild(addElement);
}

addToList();