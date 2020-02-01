$().ready(function () {
    $(".btnClick").click(function () {
        document.location.href = $(this).attr("href");
    });

})




var s = (function () {



    function validation(address, speaker) {
        var title = '';
        var body = '';

        if (address == '') {
            title = "Address Error"
            body = "Please enter your Address"
        } else if (speaker == '') {
            title = "Speaker Error"
            body = "Please Choose Speaker"
        }

        if (title == '') {
            return true
        } else {
            bootbox.alert({
                size: "small",
                title: title,
                message: body,
                callback: function () { }
            })
        };

        return false;

    }

    function setBtnValue(element, title) {
        element = '#' + element
        title = $(element).data(title)
        $(element).text(title)
    }

    function scanSpeakers(element) {
        var found = false;
        var c = s.getSpeakers('/speaker/api/speakerlist', function result(d) {
            if (!found) {
                $('#' + element).empty();
            }
            found = true;
            $('#' + element).append(`<option value="${d.name}">
                                       ${d.name}
                                  </option>`);
        });
    }




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
        updateSettings: function (url, address, speaker, method, timezone, btn, callback) {
            //$('#' + btn).prop('disabled', true)
            setBtnValue(btn, "loading-title")
            var r = validation(address, speaker)
            if (!r) {
                setBtnValue(btn, "title")
                return false; // Validation Error Occured
            }

            $.ajax({
                url: url,
                dataType: 'text',
                method: 'POST',
                data: { 'address': address, 'speaker': speaker, 'method': method, 'timezone': timezone },
                success: function (d) {
                    if (d == "Success") { // All Went Well
                        bootbox.alert({
                            size: "small",
                            title: "Device Conifgured",
                            message: "Configured Successfully",
                            callback: function () { }
                        })
                        setBtnValue(btn, "title")
                        callback();
                    } else { // API error Occured
                        setBtnValue(btn, "title")
                        bootbox.alert({
                            size: "small",
                            title: "Error Occured",
                            message: "Please Try Again!("+ d +")",
                            callback: function () { }
                        })
                    }

                },
                error: function (request, textStatus, errorThrown) {
                    //alert(textStatus);
                },
                complete: function (request, textStatus) { //for additional info
                    //alert(request.responseText);
                    //alert(textStatus);
                }
            });

        },
        updateAdhanSettings: function(url,s, btn) {            
            setBtnValue(btn, "loading-title")
            $.ajax({
                url: url,
                //dataType: 'application/json; charset=utf-8',
                method: 'POST',
                data: { 'AdhanSettings': JSON.stringify(s) },
                success: function (d) {

                    setBtnValue(btn, "title")

                    bootbox.alert({
                    size: "small",
                    title: 'Adhan Settings',
                    message: 'Settings Updated.',
                    callback: function () {  }
                        });
                },
                error: function (request, textStatus, errorThrown) {
                    setBtnValue(btn, "title")
                     //alert(textStatus);
                },
                complete: function (request, textStatus) { //for additional info
                    //alert(request.responseText);
                    //alert(textStatus);
                }
            });
        },
        getSettings: function (url, id, result) {
            $.ajax({
                url: url,
                dataType: 'text',
                method: 'GET',
                data: { 'id': id },
                success: function (d) {
                    result(d);
                },
                error: function (jqXHR, exception) {
                    //alert(jqXHR.status)
                }
            });
        },
        populateSurahs: function (molvi, selector) {

            url = 'https://server6.mp3quran.net/{molvi}/{surah}.mp3';

            $.getJSON("/static/json/surah.json", function (data) {
                var items = [];
                $.each(data, function (key, val) {
                    _url = url.replace('{molvi}', molvi).replace('{surah}', data[key].index);
                    $('#' + selector).append('<option value="' + _url + '">' + data[key].title + ' - [Verses ' + data[key].count + '] </option>');
                });

            });
        },
        dbConfigCheck: function (dbVal) {
     
            if ( dbVal=='') {

                bootbox.alert({
                    size: "small",
                    title: 'No Speaker Selected',
                    message: 'Please select a speaker from configuration tab.',
                    callback: function () { $('#home-tab').tab('show'); }
                });
                
            }
        },
        scanSpeakers: function (ele) {
            scanSpeakers(ele);
        }

    }



})();

