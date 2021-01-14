$('#add-edit-post-btn').click(function () {
    var url = "/redactor-zone/forum/create-post"
    const data = {
        "post_groups":$('#datalistOptions').val(),
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
        "post_content":$('#add-commentary').val(),
        "creation_time": now.toUTCString(),
        "modification_time": now.toUTCString() 
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

$.get('/api/users', function(data){
    var id = $(".user-info").data("id");
    for (let user in data){
        if (id == user['id']){
            $('.user-info').append(`
            <h2>${user['username']}</h2>
            `);
        }else{
            $('.user-info').append(`
            <h2>No name</h2>
            `);
        }
        
    }
})