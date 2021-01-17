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
      <button  type="button" class="btn btn-light delete-thrash"
            data-url="/redactor-zone/delete-note/${note_id}">
      <i class="fa fa-trash"></i>
      </button>
    `);
  })
})


// deleting notes
$('.delete-thrash').click(function () {
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


// articles on dashboard
$.get('/redactor-zone/api/user-articles', function(data){

  for( let article of data.slice(-3)) {
    $('#dashboard-articles').append(`
    <div class="row justify-content-center">
        <div class="card w-75">
          <div class="card-body">
            <h5 class="card-title"> 
              <a class="article-link" href="/redactor-zone/user-article/${article['article_id']}">
              <b>${article['title']}</b>
              </a>
            </h5>
            <p class="card-text">
            ${article['content']}
            </p>
          </div>
        </div>   
      </div>   
    `);
  } 
})


$.get('/redactor-zone/api/all-articles', function(data) {
  retreivePosts();
  function retreivePosts(){
      for (let article of data){
          var content = article['content'].length > 140 ? article['content'].substring(0,140)+'...' : article['content']
          var title = article['title'].length > 40 ? article['title'].substring(0,40)+'...' : article['title']
          $('#articles-container-append').append(`
          <div class="row justify-content-center c-2" style="margin-top: 30px;">
              <div class="col-sm-4">
                  <div class="card border-danger text-dark mb-3">
                      <div class="container-fluid">
                        <div class="card-body">
                          <h5 class="card-title">${article['username']}</h5>
                          <p class="card-text"><small>Last modified: ${article['article_modification_time']}</small></p>
                        </div>
                      </div>
                  </div>
              </div>
              <div class="col">
                     <div style="width: fit-content;">
                          <h6>Article title: </h6>
                          <a href="/redactor-zone/user-article/${article['article_id']}">
                              <h3 >${title}</h3>
                          </a>
                     </div>
                      <article>
                          <span>
                              ${content}
                          </span>
                      </article>
              </div>
          </div>
      
          `);
      }
  }


})