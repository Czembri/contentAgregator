
$.get("/api/v1/en/bbc", function(data) {
    setTimeout(fetchNewses, 2000);
    function fetchNewses() {
        $('.newses').empty();
        for (let news of data){
            $('.newses').append(`
            <a class="news-link" href="https://www.bbc.com${ news['Link'] }"><p>${ news['Description'] }</p></a>
            `);
        }
    }
});