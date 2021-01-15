$.get("/api/v1/en/cnn", function(data) {
    setTimeout(fetchNewses, 2000);
    function fetchNewses() {
        $('.newses').empty();
        for (let news of data){
            var descr = news['Description'][0];
            $('.newses').append(`
            <a class="news-link" href="https://edition.cnn.com${ news['Link'] }">
                <h5 class="cnn-descr">${ descr }</h5>
            </a>
            `);
        }
    }
});