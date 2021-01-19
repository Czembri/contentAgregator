function getData () {
    var url = $('.newses').attr('data-url');
    $.get(url, function(data) {
        setTimeout(fetchNewses, 2000);
        function fetchNewses() {
            $('.newses').empty();
            for (let news of data){
                $('.newses').append(`
                <a class="news-link" href="https://news.google.com${ news['Link'] }">
                    <p class="descr">${ news['Description'] }</p>
                </a>
                `);
            }
        }
    });
}

getData();