var colors = ["#4285f4", "#ea4335", "#fbbc05", "#34a853"], idx;

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
