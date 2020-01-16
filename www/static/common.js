$().ready(function () {
    $(".btnClick").click(function () {
        document.location.href = $(this).attr("href");
    });

})




var s = (function () {


    return {
        getSpeakers: function getChromeCastSpeakers(url, result) {
            $.getJSON(url, function (data) {

                $.each(data, function (key, val) {
                    result(val)
                });


            });

        },
        playMedia: function (url, device, mediaUrl, result) {

            $.ajax({
                url: url,
                dataType: 'text',
                method: 'GET',
                data: { 'deviceName': device, 'mediaUrl': mediaUrl },
                success: function (d) {
                    result(d);
                },
                error: function (request, textStatus, errorThrown) {
                    // alert(textStatus);
                },
                complete: function (request, textStatus) { //for additional info
                    //alert(request.responseText);
                    //alert(textStatus);
                }
            });

        },
        populateSurahs: function (molvi, selector) {

            url = 'https://server6.mp3quran.net/{molvi}/{surah}.mp3';

            $.getJSON("/static/json/surah.json", function (data) {
                var items = [];
                $.each(data, function (key, val) {
                    _url = url.replace('{molvi}', molvi).replace('{surah}', data[key].index);
                    $('#' + selector).append('<option value="' + _url + '">' + data[key].title + ' - [Verses ' + data[key].count +'] </option>');
                });

            });



        }

    }



})();

