$.get("/api/v1/pl/rmf", function(data) {
    setTimeout(fetchNewses, 2000);
    function fetchNewses() {
        $('.newses').empty();
        for (let news of data){
            $('.newses').append(`
            <a class="news-link" href="#"><p>${ news['Description'] }</p></a>
            `);
        }
    }
});