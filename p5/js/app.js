$(".button-collapse").sideNav();
//------------------------------------
var map;          //Map information
var markers = []; //All Markers
var VM;           //View Model
var selectedMarker  = "00FF00",
unselectedMarker = "FF0000";
var largeInfowindow;
//-----------------------------------
function initMap() {

    //Styles of the map
    var styles = [
          {
            featureType: 'water',
            stylers: [
              { color: '#19a0d8' }
            ]
          },{
            featureType: 'administrative',
            elementType: 'labels.text.stroke',
            stylers: [
              { color: '#ffffff' },
              { weight: 6 }
            ]
          },{
            featureType: 'administrative',
            elementType: 'labels.text.fill',
            stylers: [
              { color: '#e85113' }
            ]
          },{
            featureType: 'road.highway',
            elementType: 'geometry.stroke',
            stylers: [
              { color: '#efe9e4' },
              { lightness: -40 }
            ]
          },{
            featureType: 'transit.station',
            stylers: [
              { weight: 9 },
              { hue: '#e85113' }
            ]
          },{
            featureType: 'road.highway',
            elementType: 'labels.icon',
            stylers: [
              { visibility: 'off' }
            ]
          },{
            featureType: 'water',
            elementType: 'labels.text.stroke',
            stylers: [
              { lightness: 100 }
            ]
          },{
            featureType: 'water',
            elementType: 'labels.text.fill',
            stylers: [
              { lightness: -100 }
            ]
          },{
            featureType: 'poi',
            elementType: 'geometry',
            stylers: [
              { visibility: 'on' },
              { color: '#f0e4d3' }
            ]
          },{
            featureType: 'road.highway',
            elementType: 'geometry.fill',
            stylers: [
              { color: '#efe9e4' },
              { lightness: -25 }
            ]
          }
    ];

    //Map init
    map = new google.maps.Map(document.getElementById('map'),{
        center: {lat: 30.05152570239465, lng: 31.222587772460884},
        zoom: 15,
        styles: styles
    });

    //Info Window
    largeInfowindow = new google.maps.InfoWindow();

    //View Model
    VM = new AppViewModel();
    ko.applyBindings(VM, document.getElementById("locations"));
}

function googleError(){
    document.getElementById('map').innerHTML = "Map didnt Worked!";
}

//List of locations
var Locations = [
	{
        name: 'Cairo tower',
        lat: 30.045915,
        lng: 31.22428979999995,
        address: 'Zamalek, Cairo Governorate, Egypt',
        index: 0,
        fsid: "4c3c3e06a9509c74150c395b"
    },
	{
        name: 'Cairo opera house',
        lat: 30.0426678,
        lng: 31.223988299999974,
        address: 'Zamalek, Cairo Governorate, Egypt',
        index: 1,
        fsid: "4c963c5303413704fd8982ef"
    },
	{
        name: 'Tahrir Square',
        lat:  30.0443967,
        lng: 31.235717300000033,
        address: 'El-Tahrir Square, Qasr Ad Dobarah, Qasr an Nile, Cairo Governorate, Egypt',
        index: 2,
        fsid: "4cb48a7e1463a143dfb7bba9"
    },
    {
        name: 'Zamalek Sporting Club',
        lat:  30.0593895,
        lng: 31.204958799999986,
        address: 'Gazirat Mit Oqbah, Al Agouzah, Giza Governorate, Egypt',
        index: 3,
        fsid: "4ccae6fb33d3721e01d22c8b"

    },
    {
        name: 'Egyptian Museum',
        lat:  30.0478468,
        lng: 31.233649300000025,
        address: 'Ismailia, Qasr an Nile, Cairo Governorate, Egypt',
        index: 4,
        fsid: "4b653727f964a5203ee92ae3"
    }
];

//Knockout's Model
var AppModel = function(map, data) {

    //Filling Map Data
    this.name = ko.observable(data.name);
    this.index = ko.observable(data.index);
    this.address = ko.observable(data.address);
    this.lat = ko.observable(data.lat);
    this.lng = ko.observable(data.lng);

    //Marker init
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(data.lat, data.lng),
        icon: makeMarkerIcon(unselectedMarker),
        animation: google.maps.Animation.DROP,
        foursquareid: data.fsid
    });


    //Click Listener For showing Info window for clicked marker
    google.maps.event.addListener(marker, 'click', function(){
        clicked_item = VM.locationList()[data.index];
        locationClicked(marker,clicked_item);
        showInfoWindow(marker,clicked_item);
    });

    //Set Visibillity of the map
    this.isVisible = ko.observable(false);
    this.isVisible.subscribe(function(State){
        if(State){
            marker.setMap(map);
        }
        else{
            marker.setMap(null);
        }
    });

    this.isVisible(true);
    markers.push(marker);
};

//Knockout's View Model
var AppViewModel = function() {
    var self = this;
    this.searchResult = ko.observable(''); //Data bind for searchText
    this.locationList = ko.observableArray([]); //List of all Locations
    this.errorMessage = ko.observable();
    //Adding all locations into location list
    Locations.forEach(function(locationItems){
        self.locationList.push(new AppModel(map, locationItems));
    });

    //Filtering for all locations
    self.LocationMenu = ko.computed(function () {
        var matchingList;
        var searchText = self.searchResult().toLowerCase();
        if (!searchText) {
            matchingList = self.locationList();
            matchingList.forEach(function(loc){
                loc.isVisible(true);
            });
            return matchingList;
        }
        else{
            return ko.utils.arrayFilter(self.locationList(), function (loc) {
                matchingList = loc.name().toLowerCase().indexOf(searchText) !== -1;
                loc.isVisible(matchingList);
                toggleSelectedMarker(null);
                return matchingList;
            });
        }
    });

    markers.forEach(function(marker){
        addMarkerInfo(marker);
    });

    //Item location list clicked
    this.setSelected = function(loc){
        closeInfoWindow();
        locationClicked(markers[loc.index()], loc);
        showInfoWindow(markers[loc.index()], loc);
    };
};

//function to make default and highlighted marker icon
function makeMarkerIcon(markerColor) {
    var markerImage = new google.maps.MarkerImage(
        'http://chart.googleapis.com/chart?chst=d_map_spin&chld=1.15|0|' + markerColor +
        '|40|_|%E2%80%A2',
        new google.maps.Size(21, 34),
        new google.maps.Point(0, 0),
        new google.maps.Point(10, 34),
        new google.maps.Size(21, 34));
    return markerImage;
}

function locationClicked(marker, clicked_item){
    var latLng = marker.getPosition(); // marker location
    map.panTo(latLng); // change map center to the marker location
    toggleSelectedMarker(marker);
    marker.setAnimation(google.maps.Animation.BOUNCE); //Bounce marker when clicked
    setTimeout(function(){ marker.setAnimation(null); }, 900); //set timer for bouncing
}

function toggleSelectedMarker(marker){
    for (i=0; i < markers.length; i++){
        markers[i].setIcon(makeMarkerIcon(unselectedMarker));
    }
    if (marker){
        marker.setIcon(makeMarkerIcon(selectedMarker));
    }
}

function closeInfoWindow(){
    if(largeInfowindow !== null && typeof largeInfowindow !== 'undefined'){
        largeInfowindow.close();
    }
}

function addMarkerInfo(marker){
    $.ajax({
        url: "https://api.foursquare.com/v2/venues/" + marker.foursquareid + '?client_id=4PGUZ0MSOKMVW2CWWKKY3ENH2VSG5GUPAWSBXCZIT0FN5FZ1&client_secret=JWPZTBJRH2BRIPEI5K0TGCX3UQ4VCRDFRCKILBIUCFGUT1M5&v=20161016',
        dataType: "json",
        success: function( response ){
            result = response.response.venue;
            if(result.hasOwnProperty('rating')){
                marker.rating = result.rating;
            }
            else{
                marker.rating = "Error in fetching rating!";
            }
        },
        error: function( e ){
            VM.errorMessage("FourSquare is unable to send data !!");
        }
    });
}

function showInfoWindow(marker , clicked_item){
    var format_marker_info =  '<h4><b>' + clicked_item.name() + '</b></h4></span>' + '<h6>' + clicked_item.address() + '</h6>' + '<br>'+format_rating(marker);
    largeInfowindow.setContent(format_marker_info);
    largeInfowindow.open(map, marker);
}

function format_rating(marker){
    if (marker.rating === "" || marker.rating === undefined) {
        return "No rating";
    } else {
        return "Rating: " + marker.rating + "/10";
    }
}