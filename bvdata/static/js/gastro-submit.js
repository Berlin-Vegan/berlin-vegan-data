$(document).ready(function(){
    var current = 1,current_step,next_step,steps;
    steps = $("fieldset").length;

    var lat = null;
    var lon = null;

    $("#step1").click(function(){
        var name = document.getElementById("id_name");
        var street = document.getElementById("id_street");
        var citycode = document.getElementById("id_cityCode");
        var vegan = document.getElementById("id_vegan");
        var telephone = document.getElementById("id_telephone");
        var email = document.getElementById("id_email");
        var website = document.getElementById("id_website");

        var list = [name, street, citycode, vegan, telephone, email, website];


        if(valid(list))
        {
            current_step = $(this).parent();
            next_step = $(this).parent().next();
            next_step.show();
            current_step.hide();
            setProgressBar(++current);

            if($("#id_latCoord").val() === '' || $("#id_longCoord").val() === '')
            {
                var val_street = $('#id_street').val().replace(/ /g, '+');
                var val_citycode = $('#id_cityCode').val().replace(/ /g, '+');
                var val_city = $('#id_city').val().replace(/ /g, '+');

                var geocode = 'https://nominatim.openstreetmap.org/search?format=json&limit=1&q='
                    + val_street + ',' + val_citycode + ',' + val_city;
                $.getJSON(geocode, function(data) {
                    if(data[0])
                    {
                        lat = data[0].lat;
                        lon = data[0].lon;

                        //set lat long in the input fields
                        $('#id_latCoord').val(lat);
                        $('#id_longCoord').val(lon);

                        // set marker location and center map at new location
                        myMarker.setLatLng(new L.LatLng(lat, lon));
                        map.panTo(new L.LatLng(lat, lon));
                    }

                });
            }
            map.invalidateSize();
        }

    });

    $("#step2").click(function(){
        var district = document.getElementById("id_district");
        var lat = document.getElementById("id_latCoord");
        var long = document.getElementById("id_longCoord");
        var publictransport = document.getElementById("id_publicTransport");

        var list = [district, publictransport];

        if($('#id_latCoord').val() && $('#id_longCoord').val())
        {
            $("#map").removeClass("border border-danger");
            if(valid(list))
            {
                current_step = $(this).parent();
                next_step = $(this).parent().next();
                next_step.show();
                current_step.hide();
                setProgressBar(++current);
            }
        }
        else
        {
            $("#map").addClass("border border-danger");
        }

    });

    $("#step3").click(function(){
        var openingMon = document.getElementById("id_openingMon");
        var openingTue = document.getElementById("id_openingTue");
        var openingWed = document.getElementById("id_openingWed");
        var openingThu = document.getElementById("id_openingThu");
        var openingFri = document.getElementById("id_openingFri");
        var openingSat = document.getElementById("id_openingSat");
        var openingSun = document.getElementById("id_openingSun");

        var closingMon = document.getElementById("id_closingMon");
        var closingTue = document.getElementById("id_closingTue");
        var closingWed = document.getElementById("id_closingWed");
        var closingThu = document.getElementById("id_closingThu");
        var closingFri = document.getElementById("id_closingFri");
        var closingSat = document.getElementById("id_closingSat");
        var closingSun = document.getElementById("id_closingSun");

        var commentOpen = document.getElementById("id_commentOpen");

        var list = [
            openingMon, openingTue, openingWed, openingThu, openingFri, openingSat, openingSun,
            closingMon, closingTue, closingWed, closingThu, closingFri, closingSat, closingSun,
            commentOpen
        ];

        if(valid(list))
        {
            current_step = $(this).parent();
            next_step = $(this).parent().next();
            next_step.show();
            current_step.hide();
            setProgressBar(++current);
        }
    });

    $("#step4").click(function(){
        var comment = document.getElementById("id_comment");
        var commentEnglish = document.getElementById("id_commentEnglish");

        var list = [comment, commentEnglish];

        if(valid(list))
        {
            current_step = $(this).parent();
            next_step = $(this).parent().next();
            next_step.show();
            current_step.hide();
            setProgressBar(++current);
        }
    });

    $("#step5").click(function(){

        var seatsOutdoor = document.getElementById("id_seatsOutdoor");
        var seatsIndoor = document.getElementById("id_seatsIndoor");

        var list = [seatsOutdoor, seatsIndoor];

        if(valid(list))
        {
            current_step = $(this).parent();
            next_step = $(this).parent().next();
            next_step.show();
            current_step.hide();
            setProgressBar(++current);
        }
    });



    $(".previous").click(function(){
        current_step = $(this).parent();
        next_step = $(this).parent().prev();
        next_step.show();
        current_step.hide();
        setProgressBar(--current);
    });

    setProgressBar(current);
    // Change progress bar action
    function setProgressBar(curStep){
        var percent = parseFloat(100 / steps) * curStep;
        percent = percent.toFixed();
        $(".progress-bar").css("width",percent+"%").html(percent+"%");
    }

});

function valid(list) {
    var is_valid = true;
    for(var i = 0; i<list.length; i++)
    {
        if (list[i].validity.valid)
        {
            list[i].classList.remove('is-invalid');
        }
        else
        {
            is_valid = false;
            list[i].classList.add('is-invalid');
        }
    }
    return is_valid;
}


//map
var options = {
    center: [52.52194895, 13.4134887482193],
    zoom: 17
};

var map = L.map('map', options);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: 'OSM'}).addTo(map);

var myMarker = L.marker([52.52194895, 13.4134887482193], {draggable: true})
        .addTo(map)
        .on('dragend', function(e) {
            document.getElementById('id_latCoord').value=e.target._latlng['lat'];
            document.getElementById('id_longCoord').value=e.target._latlng['lng'];
        });