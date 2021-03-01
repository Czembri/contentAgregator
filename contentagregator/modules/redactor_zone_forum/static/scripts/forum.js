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
    getAvatar();
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

    function getAvatar(){
        var username = ''
        for (let post of data){
            if (post['post_id'] == post_id){
                username = post['username'][0];
            }
        }
        $('#add-avatar').attr('src', `/static/img/letters/${username.toUpperCase()}.png`)
        
    }

    function checkIfEqual () {
        if ( $('.edit').data('user') ){
            $('.btn-edit').removeAttr("style");
        }
    }

    

    function appendTo(post, content, title, usr_post_id){
        var avatar = post['username'].slice(0,1)

        $('#forum-container-explore').append(`
        <div class="row justify-content-center c-2" style="margin-top: 30px;">
            <div class="col-sm-6">
                <div class="card mb-3">
                    <div class='container-fluid'>
                        <div class="card-body">
                            <img class="post-avatar" src="/static/img/letters/${avatar.toUpperCase()}.png">
                            <h5 class="card-title">${post['username']}</h5>
                            <p class="card-text"><small class="mod-time">Last modified: ${post['post_modification_time']}</small></p>
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
        // var dict = {}
        // var list = []
        for (let post of data.slice(0, 4)){
            var content = post['content'].length > 140 ? post['content'].substring(0,140)+'...' : post['content']
            var title = post['title'].length > 40 ? post['title'].substring(0,40)+'...' : post['title']

            //     dict = {
            //         'title':title,
            //         'content':content,
            //         'username':post['username'],
            //         'last_mod':post['post_modification_time']
            //     }
            // list.push(dict);
            var avatar = post['username'].slice(0,1)
            appendPosts(content, 
                title, 
                post['username'],
                post['post_modification_time'], 
                post['post_creation_time'], 
                post['post_id'], 
                post['user_id'], 
                avatar
            );

        }

    }
})


function appendPosts (content, title, username, last_modified, created, post_id, user_id, avatar) {
    if ($('div.posts-container-1')[0]){
        $('.posts-container-1').append(`
        <div class="container">
            <div class="row justify-content-center c-2" style="margin-top: 30px;">
                <div class="col-sm-6">
                    <div class="card mb-3">
                        <div class='container-fluid'>
                            <div class="card-body">
                                <img class="post-avatar" src="/static/img/letters/${avatar.toUpperCase()}.png">
                                <div style="width:fit-content" class="row align-items-end">
                                    <a href="/user/${username}/${user_id}">
                                        <h5 class="card-title">${username}</h5>
                                    </a>
                                </div>   
                            </div>
                            <div class="card-footer">
                                <span class="card-text">
                                    <small class="mod-time">
                                        Last modified: ${last_modified.slice(0,26)}
                                    </small>
                                </span>
                                <span class="card-text float-left">
                                    <small class="mod-time">
                                        Created: ${created.slice(0,26)}
                                    </small>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div style="width: fit-content;">
                            <h6>Post title: </h6>
                            <a href="/redactor-zone/forum/show-post/${post_id}">
                                <h3 >${title}</h3>
                            </a>
                    </div>
                        <article>
                            <span>
                                ${content}
                            </span>
                        </article>
                </div>
                <div class="col edit" data-user=${user_id} data-post=${post_id}>
                    <a style="display:None;" href="/redactor-zone/forum/edit-post/${post_id}" class="btn btn-light btn-edit">Edit post</a>
                </div>
            </div>
        </div>
        `);
        
    }
        
    
}
