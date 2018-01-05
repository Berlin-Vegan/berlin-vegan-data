var latdata = document.getElementById('id_latCoord').getAttribute('value');
var longdata = document.getElementById('id_longCoord').getAttribute('value');

var options = {
    center: [latdata, longdata],
    zoom: 17
};

var map = L.map('map', options);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {attribution: 'OSM'}).addTo(map);


var myMarker = L.marker([latdata, longdata], {draggable: true})
.addTo(map)
.on('dragend', function(e) {
    document.getElementById('id_latCoord').value=e.target._latlng['lat'];
    document.getElementById('id_longCoord').value=e.target._latlng['lng'];
});