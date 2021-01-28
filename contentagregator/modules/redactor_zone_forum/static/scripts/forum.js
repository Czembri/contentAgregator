$('#add-edit-post-btn').click(function () {
    var url = "/redactor-zone/forum/create-post"
    const data = {
        "post_groups":$('#post-group').val(),
        "post_title": $('#post-title').val(),
        "post_content":$('#post-content').val(),
        "post_attachment":$('#post-attachments').val()
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

$('#edit-post-btn').click(function () {
    var url = $('#edit-post-btn').attr('data-id');
    const data = {
        "post_title": $('#post-title').val(),
        "post_content":$('#post-content').val(),
        "post_attachment":$('#post-attachments').val()
    }
    $.ajax({
        url:url,
        type:"PUT",
        data:data,
        success: function (result){
            console.log(result);
            window.location.href = `/redactor-zone/forum/show-post/${result['post_id']}`
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
            if (isNaN(user_id)){
                appendTo(post, content, title, post['user_id']);
            } else {
                if (user_id == post['user_id']){
                    appendTo(post, content, title, post['user_id']);
                }
                else {
                    continue
                }
                
            }

        }
    }

    function checkIfEqual (post_id) {
        if ( $('.edit').data('user') ){
            $('.btn-edit').removeAttr("style");
        }
    }

    function appendTo(post, content, title, usr_post_id){
        $('#forum-container-explore').append(`
        <div class="row justify-content-center c-2" style="margin-top: 30px;">
            <div class="col-sm-6">
                <div class="card mb-3">
                    <div class='container-fluid'>
                        <div class="card-body">
                            <h5 class="card-title">${post['username']}</h5>
                            <p class="card-text"><small>Last modified: ${post['post_modification_time']}</small></p>
                        </div>
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
            <div class="col edit" data-user=${user_id} data-post=${usr_post_id}>
                <a style="display:None;" href="/redactor-zone/forum/edit-post/${post['post_id']}" class="btn btn-light btn-edit">Edit post</a>
            </div>
        </div>
    
        `);
        checkIfEqual();
    }


})


$.get('/redactor-zone/forum/api/posts', function(data) {
    retreivePosts();
    function retreivePosts(){
        var dict = {}
        var list = []
        for (let post of data.slice(0, 4)){
            var content = post['content'].length > 140 ? post['content'].substring(0,140)+'...' : post['content']
            var title = post['title'].length > 40 ? post['title'].substring(0,40)+'...' : post['title']

                dict = {
                    'title':title,
                    'content':content,
                    'username':post['username'],
                    'last_mod':post['post_modification_time']
                }
            list.push(dict);
        }
        appendPosts(list);

    }
})


function appendPosts (list) {
    if ($('div.posts-container-1')[0]){
        $('.posts-container-1').append(`
        <div class="row justify-content-center" style="margin-top: 30px;">
            <div class="col">
                <div class="row justify-content-center">
                    <div class="card mb-3">
                        <div class='container-fluid'>
                            <div class="card-body">
                                <h5 class="card-title">${list[0]['title']}</h5>
                                <p class="card-text"><small>${list[0]['content']}</small></p>
                            </div>
                            <div class="card-footer text-muted">
                            ${list[0]['username']}: ${list[0]['last_mod']}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="card mb-3">
                        <div class='container-fluid'>
                            <div class="card-body">
                                <h5 class="card-title">${list[1]['title']}</h5>
                                <p class="card-text"><small>${list[1]['content']}</small></p>
                            </div>
                            <div class="card-footer text-muted">
                            ${list[1]['username']}: ${list[1]['last_mod']}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <div class="card mb-3">
                        <div class='container-fluid'>
                            <div class="card-body">
                                <h5 class="card-title">${list[2]['title']}</h5>
                                <p class="card-text"><small>${list[2]['content']}</small></p>
                            </div>
                            <div class="card-footer text-muted">
                            ${list[2]['username']}: ${list[2]['last_mod']}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col d-flex justify-content-center">
                <div class="card mb-3">
                    <div class='container-fluid'>
                        <div class="card-body">
                            <h5 class="card-title">${list[3]['title']}</h5>
                            <p class="card-text"><small>${list[3]['content']}</small></p>
                        </div>
                        <div class="card-footer text-muted">
                        ${list[3]['username']}: ${list[3]['last_mod']}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        `);
        
    }
        
    
}