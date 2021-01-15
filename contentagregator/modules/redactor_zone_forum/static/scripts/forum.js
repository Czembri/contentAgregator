$('#add-edit-post-btn').click(function () {
    var url = "/redactor-zone/forum/create-post"
    const data = {
        "post_groups":$('#post-group').val(),
        "post_title": $('#post-title').val(),
        "post_content":$('#post-content').val(),
        "post_attachments[]":$('#post-attachments').val()
    }
    $.ajax({
        url:url,
        type:"POST",
        data:data,
        success: function (result){
            console.log(result);
            location.href = `/redactor-zone/forum/show-post/${result['post_id']}`
        },
        error: function (error){
            console.log(error);
        }
    })
    
})

$('#add-commentary-btn').click(function () {
    var post_id = $(this).data("post");
    var user_id = $(this).data("user");
    var url = `/redactor-zone/forum/add-comment/${post_id}`
    var now = new Date()
    const data = {
        "user_id": user_id,
        "post_id": post_id,
        "add_commentary":$('#add-commentary').val(),
        "creation_time": now.toUTCString(),
        "modification_time": now.toUTCString() 
    }
    var request = $.ajax({
        url:url,
        type:"POST",
        data:data,
        success: function (result){
            location.href = `/redactor-zone/forum/show-post/${result['post_id']}`
        },
        error: function (error){
            console.log(error);
        }
    })
    
})

$.get('/redactor-zone/forum/api/posts', function(data) {
    retreivePosts();
    function retreivePosts(){
        for (let post of data){
            var content = post['content'].length > 140 ? post['content'].substring(0,140)+'...' : post['content']
            var title = post['title'].length > 40 ? post['title'].substring(0,40)+'...' : post['title']
            $('#forum-container-explore').append(`
            <div class="row justify-content-center c-2" style="margin-top: 30px;">
                <div class="col-sm-4">
                    <div class="card border-danger mb-3">
                        <div class="card-body">
                        <h5 class="card-title">${post['username']}</h5>
                        <p class="card-text"><small>Last modified: ${post['post_modification_time']}</small></p>
                        </div>
                    </div>
                </div>
                <div class="col">
                       <div style="width: fit-content;">
                            <h6>Post title: </h6>
                            <a href="/redactor-zone/forum/show-post/${post['post_id']}">
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