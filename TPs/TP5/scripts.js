tasks = Array();

// task format should be [name, state]
let newTask;
newTask = Array();
newTask.push("Hello", false);
tasks.push(newTask);
newTask = ["Autre test", true];
tasks.push(newTask)


/**
 * Updates the interface
 */
function updateUI(){
    updateSubtitle();
    displayTasks();
}


/**
 * Update inner HTML describing number of tasks to do depending on the presence of tasks.
 */
function updateSubtitle() {
    let doc = document.getElementById("sub");
    
    if (tasks.length == 0){
        doc.innerHTML = "Nothing to do! Good job";
    }
    else {
        let notDone = 0;
        for (let i = 0; i < tasks.length; i++) {
            if (! tasks[i][1]){
                notDone++;
            }
        }
        doc.innerHTML = "Total: " + tasks.length + " - Unfinished: " + notDone
    }
}

/**
 * Displays tasks of todo list
 */
function displayTasks() {
    let stringTable = "";
    
    // Loop on all tasks and add each one of them to the string representing the html
    for (let i = 0; i < tasks.length; i++) {
        stringTable += formatTask(tasks[i], i);
        //console.log(stringTable);
    }

    // Change HTML
    document.getElementById("tasks").innerHTML = stringTable;
}

/**
 * Returns a formated string representing the task fitting the HTML.
 * @param {Array} task : the task in which we are interested; format should be [name, state]
 * @param {Number} index : the index of the task in tasks
 * @returns {String} : a formated string representing the task fitting the HTML.
 */
function formatTask(task, index){
    return '<div class="row">\
        <div class="col-sm">'+ (task[1] ? "<s>": "") + task[0] + (task[1] ? "</s>" :"") +'</div> \
        <div class="col-sm"><button type="button" onclick="updateState('+ index +')"> <a class="far fa-check-square" style="color: '+ (task[1] ? "lime" : "red") +'"></a></button></div>\
        <div class="col-sm"><button type="button" onclick="removeTask('+ index +')"> <a class="fas fa-trash"></a></button> <a class="fas fa-pen"></a></div> \
        </div> <hr>'
}

/**
 * Updates the state of the specified task
 * @param {Number} taskID : index of task in tasks
 */
function updateState(taskID){
    // Change state of task
    tasks[taskID][1] = !tasks[taskID][1];

    //console.log(taskID);
    //console.log(tasks[taskID])

    updateUI();
}

/**
 * Removes the task from the list of tasks
 * @param {Number} taskID : index of task in tasks
 */
function removeTask(taskID){
    tasks.splice(taskID, 1);

    updateUI();
}

/**
 * Add a new task to list of tasks
 */
function addTask() {
    // Create task
    let newTask = Array();

}