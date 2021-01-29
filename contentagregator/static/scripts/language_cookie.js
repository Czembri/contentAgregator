document.addEventListener("DOMContentLoaded", () => {
    // Language cookie
    var enButton = document.getElementById("en")
    var plButton = document.getElementById("pl")

    function setLangCookie(lang) {
        document.cookie = "user_lang=" + lang;
    }

    function getCookie(name) {
        var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        if (match) return match[2];
      }

    enButton.addEventListener("click", function(){
        setLangCookie("en");
        location.reload();
    });

    plButton.addEventListener("click", function(){
        setLangCookie("pl");
        location.reload();
    });

    var lang = getCookie("user_lang");

  

	if(lang==='pl') lang='Polish';
	else lang='English';
    document.getElementById("lang").innerHTML = lang;
    translate(lang);
    function translate(lang){
      if ($("#lang").text() =='Polish'){
          $.get('/api/translations', function (data) {
              if (typeof markPage !== 'undefined'){
                for (let t of data){
                  if (markPage == "create"){
                    
                        $('.t-user').text(t['forum-create'][0]['Username']);
                        $('.t-group').text(t['forum-create'][0]['Group']);
                        $('.t-title').text(t['forum-create'][0]['Title']);
                        $('.t-content').text(t['forum-create'][0]['Content']);
                        $('.t-attach').text(t['forum-create'][0]['AddAttachment']);
                        $('.t-btn').text(t['forum-create'][0]['Addpost']);
                    
                  } else if (markPage == "index"){
                    $('.write-post').text(t['forum-index'][0]['Writeapost']);
                    $('.explore').text(t['forum-index'][0]['Explore']);
                    $('.go-to').text(t['forum-index'][0]['GoTo']);
                  }
                }
              }
            
          })
      }   
    }

});