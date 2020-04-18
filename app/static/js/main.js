// map initialisation
// + dummy map loading (working around maps display pb when loading it later)
var map;
function initMap()
    {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 13, lng: 13},
    zoom: 13});
    }

$("#map").hide();
$("#question").trigger("reset");
$(".spinner-border").hide();

function answer(text)
// takes a string in entry (must be DE XSS'd for security sakes!)
// returns a  DOM elm't to display the text)
    {
    return '<div class="col-sm-10 col-md-10 col-lg-9 bg-white rounded shadow-sm">\
            <div class="media text-muted pt-3">\
            <svg class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="text" aria-label="Placeholder: 32x32"><title>Placeholder</title>\
            <rect width="100%" height="100%" fill="#007bff"></rect><text x="15%" y="70%" fill="#007bff">🤖</text></svg>\
            <p class="media-body pb-3 mb-0 lh-125 large border-bottom border-gray">'+text+'</p></div></div>';
    }

function question(text)
// same as funct answer but without the icon
    {
    return '<div class="col-sm-10 col-md-10 col-lg-9 bg-white rounded shadow-sm">\
            <div class="media text-muted pt-3">\
            <svg class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="text" aria-label="Placeholder: 32x32"><title>Placeholder</title>\
            <text x="15%" y="70%" fill="black"></text>??</svg>\
            <p class="media-body pb-3 mb-0 lh-125 large border-bottom border-gray">'+text+'</p></div></div>';
    }

    $(".btn").click(function(event)
        {
        event.preventDefault();
        //filter against XSS
        var reg = new RegExp(/[<>!$'"/*%$£=+#{};\\&~]/, "g");
        var newchain = $("#textarea").val();
        newchain = newchain.replace(reg, " ");

        $("#dialog").append(question(newchain));
        $("#map2").hide(600);
        $("#map2").remove();
        $("#textarea").hide(600);
        $(".btn").hide(600);
        $(".spinner-border").show(600);
        //sending request to server : if answer status is ok add the answwer map and the wiki,
        //else only add the answer from server
        $.ajax(
            {
            url: '/question',
            data: $('.form-control').serialize(),
            type: 'POST',
            success: function(response) 
                {
                var answer_obj = JSON.parse(response)
                $("#question").trigger("reset");
                $("#textarea").show(400);
                $(".btn").show(400); 
                $(".spinner-border").hide(400);
                if (answer_obj.status === 'OK' || answer_obj.status === "OK_WIKI_FAILED")
                    {              
                    $("#gmap").append('<div class="col-sm-10 col-md-10 col-lg-9"><div id="map2"></div></div>');
                    map2 = new google.maps.Map(document.getElementById('map2'), 
                        {
                        center: {lat: answer_obj.coordinates.lat, lng: answer_obj.coordinates.lng},zoom: 13
                        });
                    var marker = new google.maps.Marker(
                        {
                        position: {lat: answer_obj.coordinates.lat, lng: answer_obj.coordinates.lng}, map: map2
                        });
                    $("#dialog").append(answer(answer_obj.adresses_answer));
                    setTimeout(()=>
                        {
                        $("#dialog").append(answer(answer_obj.wiki_answer))
                        },5000)
                    }
                else
                    {
                    $("#dialog").append(answer(answer_obj.adresses_answer));
                    }
                
                },
            error: function(error) 
                {
                warning("la requette n'as pas pu être analysée");
                }
            });

    });
    