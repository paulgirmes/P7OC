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
    {
    return '<div class="col-sm-10 col-md-10 col-lg-9 bg-white rounded shadow-sm">\
            <div class="media text-muted pt-3">\
            <svg class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="text" aria-label="Placeholder: 32x32"><title>Placeholder</title>\
            <rect width="100%" height="100%" fill="#007bff"></rect><text x="15%" y="70%" fill="#007bff">🤖</text></svg>\
            <p class="media-body pb-3 mb-0 lh-125 large border-bottom border-gray">'+text+'</p></div></div>';
    }

function question(text)
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
        $("#dialog").prepend(question($("#textarea").val()));
        $("#map2").hide(600);
        $("#map2").remove();
        $("#textarea").hide(600);
        $(".btn").hide(600);
        $(".spinner-border").show(600);
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
                    $("#dialog").prepend(answer(answer_obj.adresses_answer));
                    setTimeout(()=>
                        {
                        $("#dialog").prepend(answer(answer_obj.wiki_answer))
                        // $("#dialog:last").hide();
                        // $("#dialog:last").show(400);
                        },5000)
                    }
                else
                    {
                    $("#dialog").prepend(answer(answer_obj.adresses_answer));
                    }
                
                },
            error: function(error) 
                {
                warning("la requette n'as pas pu être analysée");
                }
            });

    });
    