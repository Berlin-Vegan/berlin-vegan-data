var lat = document.getElementById('id_latCoord').getAttribute('value') || 52.52194895;
var lon = document.getElementById('id_longCoord').getAttribute('value') || 13.4134887482193;
var district = null;

$(document).ready(function() {

    $('#getadress').click(function () {
        var street = $('#id_street').val().replace(/ /g, '+');
        var citycode = $('#id_cityCode').val().replace(/ /g, '+');
        var city = $('#id_city').val().replace(/ /g, '+');

        var geocode = 'https://nominatim.openstreetmap.org/search?format=json&limit=1&q='
            + street + ',' + citycode + ',' + city;
        $.getJSON(geocode, function(data) {
            lat = data[0].lat;
            lon = data[0].lon;

            //set lat long in the input fields
            $('#id_latCoord').val(lat);
            $('#id_longCoord').val(lon);

            // set marker location and center map at new location
            myMarker.setLatLng(new L.LatLng(lat, lon));
            map.panTo(new L.LatLng(lat, lon));
        });

    });

});

var options = {
    center: [52.52194895, 13.4134887482193],
    zoom: 17
};

var map = L.map('map', options);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: 'OSM'}).addTo(map);

var myMarker = L.marker([lat, lon], {draggable: true})
        .addTo(map)
        .on('dragend', function(e) {
            document.getElementById('id_latCoord').value=e.target._latlng['lat'];
            document.getElementById('id_longCoord').value=e.target._latlng['lng'];
        });
map.panTo(new L.LatLng(lat, lon));
