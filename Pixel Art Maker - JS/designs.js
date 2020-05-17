function makeGrid() {
    const height = document.getElementById('inputHeight').value;
    // console.log(height);
    const width = document.getElementById('inputWidth').value;
    // console.log(width);
    const table = document.getElementById('pixelCanvas');
    for (i = 1; i <= height; i++){
        const row = document.createElement('tr');
        for(j = 1; j <= width; j++){
            const cell = document.createElement('td');
            cell.addEventListener('click', function() {
                changeColor(cell);
            });
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
}


//Clears the previous grid
function removeGrid() {
    const table = document.getElementById('pixelCanvas');
    while (table.lastChild) {
        table.removeChild(table.lastChild);
    }
}


//Functionality of the Submit botton
const submit = document.getElementById('inputSubmit');
submit.addEventListener('click', function() {
    removeGrid();
    makeGrid();
});


// Select color input
function changeColor(cell) {
    const color = document.getElementById('colorPicker').value;
    if (cell.style.backgroundColor === "") {
        cell.style.backgroundColor = color;
    } else{
        cell.style.backgroundColor = "";
    }
}
