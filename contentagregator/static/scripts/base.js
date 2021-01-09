$(".nav-link").hover(function(){
    $(this).addClass("active-item")
}, function(){
    $(this).removeClass("active-item")
});

if(!localStorage['cookiesAccepted']){
    $('#cookies-modal-container').append(`
    <div class="modal fade" id="cookies-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
            </div>
            <div class="modal-body">
            <h3 class="accept-cookies-body">Accept cookies</h3>
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-light" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-dark" id="accept-cookies">Accept</button>
            </div>
        </div>
        </div>
    </div>
    `);
    $('#cookies-modal').modal({backdrop:'static', keyboard: false});
	var acceptCookiesBtn = document.getElementById("accept-cookies");	
	acceptCookiesBtn.onclick = function(){
        $('#cookies-modal').modal('toggle');
        localStorage['cookiesAccepted'] = true;
	}
}

var modalDeleteID = document.getElementById('delete-modal-view');
if (modalDeleteID){
    modalDeleteID.innerHTML = `
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <h3 class="accept-cookies-body">Are you sure?</h3>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-light" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-danger" id="delete-modal-btn">Delete</button>
            </div>
        </div>
    </div>
`
}


var currentURL = window.location.href;
var deleteModalCaller;
var deleteModalUrl;
$('#delete-modal-view').on('show.bs.modal', function(e){
	deleteModalCaller = e.relatedTarget;
	deleteModalUrl = deleteModalCaller.dataset.url;
});
$("#delete-modal-btn").click(function(){
	$.ajax({
        url: deleteModalUrl,
        type: 'DELETE',
    });
	var lastChar = currentURL.slice(-1);
	if(isNaN(lastChar)){ // if lastChar is not a digit
		var card = deleteModalCaller.parentNode.parentNode.parentNode.parentNode;
		card.remove();
		$("#delete-modal-view").modal("hide");
	}
	else{
		currentURL = redirect;
	}
});