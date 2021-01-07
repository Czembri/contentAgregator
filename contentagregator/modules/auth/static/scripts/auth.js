var i = 0;
var txt = 'I want to write the news';
var speed = 50;

window.onload = function typeWriter() {
  if (i < txt.length) {
    $('.write-news').append(txt.charAt(i));
    i++;
    setTimeout(typeWriter, speed);
  }
}