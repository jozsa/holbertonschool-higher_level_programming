$(function() {
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: function(language) {
            $("DIV#hello").text(language.hello);
        }
    });
});