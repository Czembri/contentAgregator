const src = ["Forum", "Redactor Zone"];
const url = '/api/v2/search';

const autoCompleteJS = new autoComplete({
    placeHolder: "Search...",
    data: {
        src: src
    },
    resultItem: {
        highlight: {
            render: true
        }
    },
    events: {
        input: {
            selection: (event) => {
                const selection = event.detail.selection.value;
                autoCompleteJS.input.value = selection;
                $.get(url, function(data) {
                    var uri = data[selection]["uri"];
                    console.log(uri);
                })
               
            }
        }
    }
   });
