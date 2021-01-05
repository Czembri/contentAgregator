var colors = ["#4285f4", "#ea4335", "#fbbc05", "#34a853"], idx;

$.get("/api/v1/en/google", function(data) {
    setTimeout(fetchNewses, 2000);
    function fetchNewses() {
        $('.newses').empty();
        for (let news of data){
            $('.newses').append(`
            <a class="news-link" href="https://news.google.com${ news['Link'] }"><p>${ news['Description'] }</p></a>
            `);
        }
    }
});



$(function() {
var googleTitle = $('.title'); 
var chars = googleTitle.text().split('');
googleTitle.html('');     
for(var i=0; i<chars.length; i++) {
    idx = Math.floor(Math.random() * colors.length);
    var span = $('<span>' + chars[i] + '</span>').css("color", colors[idx]);
    googleTitle.append(span);
}
});