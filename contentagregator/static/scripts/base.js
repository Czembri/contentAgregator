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