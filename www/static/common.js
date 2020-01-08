$().ready(function () {
    document.getElementById("previous").addEventListener("click", goBack);
})


function goBack() {  
    document.location.href = $(this).attr("href");
}

var s = (function () {


    return {
        getSpeakers: function getChromeCastSpeakers(url, result) {
            $.getJSON(url, function (data) {

                $.each(data, function (key, val) {
                    result(val)
                });


            });

        }
    }


})();

