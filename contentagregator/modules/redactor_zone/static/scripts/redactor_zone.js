$.get("/redactor-zone/api/user-articles", function(data) {
    var articles_count = data.length;
    var i = 0;
    function move() {
      if (i == 0) {
        i = 1;
        var elem = document.getElementById("progressionBar");
        var max_count = 50;
        var width = (articles_count * 100) / max_count;
        var id = setInterval(frame, 10);
        function frame() {
            elem.style.width = width + "%";
        }
      }
    }
   
    move();
})