let table = document.getAttributeById('sampleTable');

function insert_Tr(){
    let row = table.children.lenght;
    let tr = document.createElement('tr');
    tr.innerHtml = "<tr>Row[i] cell1</tr><tr>Row[i] cell2</tr>";
    table.append(tr);
}
function insert_Td(){
    let tr1 = document.createElement('my_tr');
    let td = document.createElement('td');
    tr1.innerHtml = "Test_TD";
    td.append(tr1);
}




