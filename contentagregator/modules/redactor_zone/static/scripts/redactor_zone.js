$( function() {
  $("#create").click(function() {
     $sticky = $('<div id="single-note" class="single-note"><textarea id="note-input">This is a sticky note you can type and edit.</textarea></div>');
    $("#note-container").append($sticky);
  });
} );


$('#accept').click(function(){
  var content = $('#note-input').val();
  var data = {"user_id":user_id, "note_content":content};
  $.post("/redactor-zone/user-notes/add-note", data, function(note_id){
    $("#single-note").toggleClass("single-note added-note");
    $(".added-note").empty();
    $(".added-note").append(`
      <textarea data-id=${note_id} readonly>${content}</textarea>
    `);
  })
})