function hide_parent(element){
  $(element).parent().remove();
}

function toggle_check(target_url, id_task, checkbox){
  var checked = checkbox.checked;
  $.ajax({
    url: target_url,
    data: JSON.stringify({ id_task, checked }),
    type: 'POST',
    contentType: "application/json",
    dataType: "json",
    success: function(response){
      checkbox.checked = response['state'];
    },
    error: function (error) {
      console.log(error);
    }
  });
}