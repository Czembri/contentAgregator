var attachment = document.getElementById( 'attachments_view' );

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

attachment.addEventListener( 'change', showFileName );

function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  var file = fileName.length > 24 ? fileName.substring(0,24) + '...' : fileName
  if ($('.current-name').text().length == 0){
    $('.display-attachment-container').append(`
    <h4 class="current-name" style="text-align: right;">Currently added:</h4>
    <span style="margin: 10px 0; width: fit-content; float:right;" class="btn btn-outline-secondary">
    ${file}
    <i class="fas fa-times"></i>
    </span>
    `);
  } else {
    $('$display-attachment-container').append(`
    <span style="margin: 10px 0; width: fit-content;" class="btn btn-outline-secondary">
    ${file}
    <i class="fas fa-times"></i>
    </span>
    `);
  }

}