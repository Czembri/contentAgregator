var attachment = document.getElementById( 'attachments_view' );


  $("#create").click( function() {
    $(".notes-container").append(
      `<div id="single-note" class="single-note">
        <textarea id="note-input">This is a sticky note you can type and edit.</textarea>
      </div>`
    );
  });


$('#accept').click(function(){
  var content = $('#note-input').val();
  var data = {"user_id":user_id, "note_content":content};
  $.post("/redactor-zone/user-notes/add-note", data, function(note_id){
    $("#single-note").toggleClass("single-note added-note");
    $(".added-note").empty();
    $(".added-note").append(`
      <textarea data-id=${note_id} readonly>${content}</textarea>
      <button  type="button" class="btn btn-light" id="delete-thrash"
            data-url="/redactor-zone/delete-note/${note_id}">
      <i class="fa fa-trash"></i>
      </button>
    `);
  })
})


// deleting notes
$('#delete-thrash').click(function () {
  $.ajax({
      url: $(this).attr('data-url'),
      type: 'DELETE',
  });
      location.href='/redactor-zone/user-notes';
  })

  // attachments

if (attachment){
  attachment.addEventListener( 'change', showFileName );
}

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
