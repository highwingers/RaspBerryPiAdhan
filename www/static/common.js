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
        playMedia: function (url,device, mediaUrl, result) {
            $.getJSON(url, {'device': device, 'media': mediaUrl} ,function (data) {
                    result(val)
            });

        }
    }


})();

