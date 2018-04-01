$(document).ready(function(){
    var current = 1,current_step,next_step,steps;
    steps = $("fieldset").length;

    var lat = null;
    var lon = null;

    $(".next").click(function(){
        current_step = $(this).parent();
        next_step = $(this).parent().next();
        next_step.show();
        current_step.hide();
        setProgressBar(++current);

    });

    $(".map").click(function(){
        var vegan = [document.getElementById("id_district")];
        var lat = document.getElementById("id_latCoord");
        var long = document.getElementById("id_longCoord");

        if($('#id_latCoord').val() && $('#id_longCoord').val())
        {
            $("#map").removeClass("border border-danger");
            if(valid(vegan))
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

    $(".getgeo").click(function(){
        var name = document.getElementById("id_name");
        var street = document.getElementById("id_street");
        var city = document.getElementById("id_city");
        var citycode = document.getElementById("id_cityCode");
        var vegan = document.getElementById("id_vegan");

        var list = [name, street, city, citycode, vegan];


        if(valid(list)){
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

L.tileLayer('https://{s}.tile.openstreetmap.org.org/{z}/{x}/{y}.png', {attribution: 'OSM'}).addTo(map);

var myMarker = L.marker([52.52194895, 13.4134887482193], {draggable: true})
        .addTo(map)
        .on('dragend', function(e) {
            document.getElementById('id_latCoord').value=e.target._latlng['lat'];
            document.getElementById('id_longCoord').value=e.target._latlng['lng'];
        });