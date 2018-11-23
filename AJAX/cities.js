$('document').ready(function() {

    var term = $('#term').val();

    $.ajax({
        url: "/suggestjson",
        type: "POST",
        dataType: "json",
        data: JSON.stringify({'term': term}),
        success: function (data) {
            alert('success');
            console.log( data );
        }
    });
});
