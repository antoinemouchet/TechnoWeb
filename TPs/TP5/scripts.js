tasks = Array();


/**
 * Updates the interface
 */
function updateUI(){
    updateSubtitle();
    displayTasks();
    cursorFocusTask();
}


/**
 * Update inner HTML describing number of tasks to do depending on the presence of tasks.
 */
function updateSubtitle() {
    let doc = document.getElementById("sub");
    
    if (tasks.length == 0){
        doc.innerText = "Nothing to do! Good job";
    }
    else {
        let notDone = 0;
        for (let i = 0; i < tasks.length; i++) {
            if (! tasks[i][1]){
                notDone++;
            }
        }
        doc.innerText = "Total: " + tasks.length + " - Unfinished: " + notDone
    }
}

/**
 * Displays tasks of todo list
 */
function displayTasks() {

    let stringTable = document.getElementById("tasks");

    // Reset table
    stringTable.innerHTML = ""

    // Loop on all tasks and add each one of them to the string representing the html
    for (let i = 0; i < tasks.length; i++) {
        stringTable.appendChild(formatTask(tasks[i], i));
        stringTable.appendChild(document.createElement("hr"))
    }

}

/**
 * @param {Array} task : the task in which we are interested; format should be [name, state]
 * @param {Number} index : the index of the task in tasks
 * @returns {HTMLDivElement} : Element representing a task in HTML
 */
function formatTask(task, index){

    // Create row
    let row = document.createElement("div");
    row.className = "row";

    let col0 = document.createElement("div");
    col0.className = "col-sm";

    let icon = document.createElement("i");
    icon.className = (task[1] ? "fas fa-check" : "fas fa-times")

    col0.appendChild(icon);

    // Column 1 with name of task
    let col1 = document.createElement("div");
    col1.className = "col-sm" + (task[1] ? " strike-through": "");
    col1.innerText = task[0];

    // Column 2 with update state button
    let col2 = document.createElement("div");
    col2.className = "col-sm";

    let button = document.createElement("button");
    button.type = "button";
    button.className = (task[1] ? "btn btn-danger" : "btn btn-success");
    button.textContent = (task[1] ? " Not done " : " Done ");
    button.onclick = () => {updateState(index)};

    let a = document.createElement("a");
    a.className= (task[1] ? " far fa-square " : "far fa-check-square");
    a.style.color = "whitesmoke";
    
    button.appendChild(a);
    col2.appendChild(button);

    // Column 3 with modification buttons
    let col3 = document.createElement("div");
    col3.className = "col-sm";

    let buttonGroup = document.createElement("div");
    buttonGroup.className = "btn-group";
    buttonGroup.role = "group";

    // Remove button
    let button2 = document.createElement("button");
    button2.type = "button";
    button2.className = "btn btn-danger";
    button2.onclick = () => {removeTask(index)};

    let a2 = document.createElement("a");
    a2.className="fas fa-trash";
    
    button2.appendChild(a2);

    // Edit button
    let button3 = document.createElement("button");
    button3.type = "button";
    button3.className = "btn btn-secondary";
    button3.onclick = () => {displayTaskForm("javascript:modifyTask(" + index +")", task[0])};

    let a3 = document.createElement("a");
    a3.className="fas fa-pen";
    button3.appendChild(a3);

    buttonGroup.appendChild(button3);
    buttonGroup.appendChild(button2);

    col3.appendChild(buttonGroup);
    
    // Apend columns to row
    row.appendChild(col0);
    row.appendChild(col1);
    row.appendChild(col2);
    row.appendChild(col3);

    return row

}

/**
 * Updates the state of the specified task
 * @param {Number} taskID : index of task in tasks
 */
function updateState(taskID){
    // Change state of task
    tasks[taskID][1] = !tasks[taskID][1];

    updateUI();
}

/**
 * Removes the task from the list of tasks
 * @param {Number} taskID : index of task in tasks
 */
function removeTask(taskID){
    // Cancel any edit happening
    endEdit();
    // Remove task
    tasks.splice(taskID, 1);

    updateUI();
}

/**
 * Add a new task to list of tasks
 */
function addTask() {
    // Create task
    let newTask = Array();
    
    // Get task name from form
    taskName = document.getElementById("task-input").value;

    // Add caracteristics to newTask
    newTask.push(taskName, false);

    // Add task to list of tasks
    tasks.push(newTask);

    // Reset value of field
    document.getElementById("task-input").value = "";
    updateUI();

}

/**
 * Generates a form to input task name
 * @param {String} action String representing the action to execute on form submit
 * @param {String} taskName name of the task to modify.
 */
function displayTaskForm(action="javascript:addTask()", taskName="") {

    let formString = "";
    
    formString += action == "javascript:addTask()" ? "<h4> Add a task </h4>" : ("<h4> Modify task: " + taskName + "</h4>");

    formString += ' <form action="'+ action +'" onsubmit="return validateTask()">\
    <input id="task-input" type="text" placeholder="Enter task name" value="'+ taskName +'">\
    <input id="submit" type="submit" value="Submit">';

    formString += (action == "javascript:addTask()" ?'' :'<input type="button" value="Cancel" onClick="javascript:endEdit()"') + '</form>';

    // Add to actual HTML
    document.getElementById("task-form").innerHTML = formString

    // Focus cursor on field
    cursorFocusTask("task-input");
}

/**
 * Places the cursor 
 * @param {String} field String representing id of field to place cursor in
 */
function cursorFocusTask(field="task-input") {
    document.getElementById(field).focus();
    document.getElementById(field).select();
}

function validateTask(field="task-input") {
    // Get value from form
    let taskName = document.getElementById(field).value;

    // Check not only whitespace
    if (taskName.trim() == ""){
        window.alert("Task can not be empty or whitespaces only");
        document.getElementById(field).value = "";
        return false;
    }

    return true;
}

/**
 * Modifies the name of the task at taskID
 * @param {Number} taskID index of task to modidy in tasks
 */
function modifyTask(taskID) {

    // Change name of task
    tasks[taskID][0] = document.getElementById("task-input").value;

   endEdit();

}

/**
 * Ends the editing of a task
 */
function endEdit(){
    // Reset task form and update UI
    displayTaskForm();
    updateUI()
}