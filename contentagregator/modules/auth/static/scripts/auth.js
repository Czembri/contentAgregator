var i = 0;
var txt = 'I want to write the news';
var speed = 50;

window.onload = function typeWriter() {
  if (i < txt.length) {
    $('.write-news').append(txt.charAt(i));
    i++;
    setTimeout(typeWriter, speed);
  }
}


$('#update-user').click(function () {
  var url = $('#update-user').attr('data-url');
  const data = {
      "fullname": $('#fullname').val(),
      "username":$('#username').val(),
      "email":$('#email').val()
  }
  $.ajax({
      url:url,
      type:"PUT",
      data:data,
      success: function (result){
          console.log(result);
          window.location.href = `/user/${username}/${user_id}`
      },
      error: function (error){
          console.log(error);
      }
  })
  
})