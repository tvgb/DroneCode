const homeIP = 'http://192.168.0.195:5000';
const droneIP = 'http://192.168.42.23:5000';
const schooleIP = 'http://10.22.117.235:5000';
// schooleIP = 'http://10.22.117.235:5000';

const imgPack = "pack2";

$("#connectToDroneImg").attr("src",`./images/${imgPack}/connect.png`);
$("#takeOffImg").attr("src",`./images/${imgPack}/takeOff.png`);
$("#landImg").attr("src",`./images/${imgPack}/land.png`);
$("#droneImg").attr("src",`./images/${imgPack}/drone.png`);


$("#connectToDroneImg").click(function() {
    sendHttpRequest('connectToDrone');
});

$("#takeOffImg").click(function() {
   sendHttpRequest('takeOff');
});

$("#landImg").click(function() {
    sendHttpRequest('land');
});

$("#abortImg").click(function() {
    sendHttpRequest('abort');
});

$("#gpsImg").click(function() {
    data = JSON.stringify({
        'latitude': null,
        'longitude': null,
        'altitude': null
    })
    sendHttpRequest('moveTo', data=data);
});

$("#forwardImg").click(function() {
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0,
        'z_movement': 0.5
    })

    sendHttpRequest('moveBy', data)
})

$("#backImg").click(function() {
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0,
        'z_movement': -0.5
    })

    sendHttpRequest('moveBy', data)
})

$("#leftImg").click(function() {
    data = JSON.stringify({
        'x_movement': -0.5,
        'y_movement': 0,
        'z_movement': 0
    })

    sendHttpRequest('moveBy', data)
})

$("#rightImg").click(function() {
    data = JSON.stringify({
        'x_movement': 0.5,
        'y_movement': 0,
        'z_movement': 0
    })

    sendHttpRequest('moveBy', data)
})

$("#upImg").click(function() {
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0.5,
        'z_movement': 0
    })

    sendHttpRequest('moveBy', data)
})

$("#downImg").click(function() {
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': -0.5,
        'z_movement': 0
    })

    sendHttpRequest('moveBy', data)
})

const addMessageToBox = function(message) {
    $("#messageBox").append(`<p class="infoMessage">${message}</p>`);

    let objDiv = document.getElementById("messageBox");
    objDiv.scrollTop = objDiv.scrollHeight;
}

const sendHttpRequest = function(request, data=null) {
    $.ajax({
        method: "POST",
        url: `${droneIP}/${request}`,
        data: data,
        contentType: "application/json"
    }).done(function(data) {
        addMessageToBox(data.message);
    });
}