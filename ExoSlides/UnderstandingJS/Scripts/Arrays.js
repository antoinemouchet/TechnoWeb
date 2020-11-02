function myFunction(){
    let my_array = Array();

    // Add elements to array
    my_array.push(1);
    my_array.push(2);
    my_array.push(3);

    // Display array
    document.getElementById("array1").innerHTML = my_array.join() + "<br>";

    // Remove last element from array
    my_array.pop();

    // Get length of array
    let arr_len = my_array.length;
    // Log length of array
    console.log(arr_len);

    // Different ways to display my_array
    document.getElementById("array2").innerHTML = my_array.join(" ") + "<br>";
    document.getElementById("array3").innerHTML = my_array.join(" : ") + "<br>";

    // Call the displayEl for each element of the array
    //my_array.forEach(displayEl);    

}

function displayEl(element, index) {
    document.write("Element at index " + index + " has value " + element + "<br>");
}
