$('.regex-matches-form').submit(function (e) { 
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

$('.regex-sub-form').submit(function (e) { 
    e.preventDefault();

    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: $(this).serialize(),
        dataType: "json",
        success: function (response) {
            $('.sub-result-block').empty();

            let newElement = $(`<div class='sub-result-block mt-4'>${response.sub_result}</div>`);
            $('.main').append(newElement);
        }
    });
});