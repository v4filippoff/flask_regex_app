$('.regex-test-form').submit(function (e) { 
    e.preventDefault();

    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: "json",
        success: function (response) {
            $('.matches-block').empty();

            let matches = response.matches.join('<br>');
            let newElement = $(`<div class='matches-block mt-4'>${matches}</div>`);
            $('.main').append(newElement);
        }
    });
});