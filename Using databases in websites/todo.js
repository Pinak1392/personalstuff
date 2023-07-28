var todolistContainer = document.getElementById("todo");
var template = $("#list-item-template").html();

for (var i = 0; i < window.localStorage.length; i++) {
    var itemName = localStorage.key(i);
    var taskHTML = template.replace("<!-- TASK_NAME -->", itemName);
    $('#todo').append(taskHTML);
}  

$('#add-task-button').click(function(event) {
  var taskName = $("#newTask").val();
  $("#newTask").val('')

  var taskHTML = template.replace("<!-- TASK_NAME -->", taskName);
  $('#todo').append(taskHTML);
  window.localStorage.setItem(taskName, '');
});

todolistContainer.addEventListener('click', function(event) {
    var targetElement = event.target;

    while (!targetElement.classList.contains("task")) {
      targetElement = targetElement.parentElement;
    }

    var checkbox = targetElement.querySelector("input");
  
    if (checkbox.checked) {
      $(targetElement).addClass("completed");

      var inText = targetElement.getElementsByTagName("label")[0].innerText;
      window.localStorage.removeItem(inText.slice(1), '');

    } else {
      $(targetElement).removeClass("completed");

      var inText = targetElement.getElementsByTagName("label")[0].innerText;
      window.localStorage.setItem(inText.slice(1), '');
    }
});
  