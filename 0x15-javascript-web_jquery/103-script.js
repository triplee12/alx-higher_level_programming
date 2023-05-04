$(document).ready(function () {
    function translateHello() {
        var languageCode = $("#language_code").val();
        $.get(
            "https://www.fourtonfish.com/hellosalut/hello/",
            { lang: languageCode },
            function (data) {
                $("#hello").html(data.hello);
            }
        );
    }

    $("#btn_translate").click(function () {
        translateHello();
    });

    $("#language_code").keypress(function (e) {
        if (e.which == 13) {
            translateHello();
        }
    });
});
