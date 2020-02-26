const homeIP = 'http://192.168.0.195:5000';
const droneIP = 'http://192.168.42.23:5000';
const schooleIP = 'http://10.22.117.235:5000';
const localIP = 'http://localhost:5000'

const imgPack = "pack2";

const MOVEMENT_UNIT = 0.25;

$("#connectToDroneImg").attr("src",`./images/${imgPack}/connect.png`);
$("#takeOffImg").attr("src",`./images/${imgPack}/takeOff.png`);
$("#landImg").attr("src",`./images/${imgPack}/land.png`);
$("#droneImg").attr("src",`./images/${imgPack}/drone.png`);


$("#connectToDroneImg").click(function() {
    addMessageToBox('Trying to connect to drone...');
    sendHttpRequest('connectToDrone');
});

$("#takeOffImg").click(function() {
    addMessageToBox('Trying to take off...');
    sendHttpRequest('takeOff');
});

$("#landImg").click(function() {
    addMessageToBox('Trying to land...');
    sendHttpRequest('land');
});

$("#abortImg").click(function() {
    addMessageToBox('Trying to abort');
    sendHttpRequest('abort');
});

$("#gpsImg").click(function() {
    addMessageToBox('Trying to move to gps coordinates');
    data = JSON.stringify({
        'latitude': null,
        'longitude': null,
        'altitude': null
    })
    sendHttpRequest('moveTo', data=data);
});

$("#forwardImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0,
        'z_movement': MOVEMENT_UNIT,
        'rotation': 0.0
    })

    sendHttpRequest('moveBy', data)
})

$("#backImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0,
        'z_movement': -MOVEMENT_UNIT,
        'rotation': 0.0
    })

    sendHttpRequest('moveBy', data)
})

$("#leftImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': -MOVEMENT_UNIT,
        'y_movement': 0,
        'z_movement': 0,
        'rotation': 0.0
    })

    sendHttpRequest('moveBy', data)
})

$("#rightImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': MOVEMENT_UNIT,
        'y_movement': 0,
        'z_movement': 0,
        'rotation': 0.0
    })

    sendHttpRequest('moveBy', data)
})

$("#upImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': MOVEMENT_UNIT,
        'z_movement': 0,
        'rotation': 0.0
    })

    sendHttpRequest('moveBy', data)
})

$("#downImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': -MOVEMENT_UNIT,
        'z_movement': 0,
        'rotation': 0.0
    })

    sendHttpRequest('moveBy', data)
})

$("#turnCounterClockwiseImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0,
        'z_movement': 0,
        'rotation': -0.19625
    })

    sendHttpRequest('moveBy', data)
})

$("#turnClockwiseImg").click(function() {
    addMessageToBox('Trying to move');
    data = JSON.stringify({
        'x_movement': 0,
        'y_movement': 0,
        'z_movement': 0,
        'rotation': 0.19625
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
        url: `${localIP}/${request}`,
        data: data,
        contentType: "application/json; charset=utf-8",
        xhrFields: {
            withCredentials: false
        },
        crossDomain: true
    }).done(function(data) {
        console.log(data);
        addMessageToBox(data.message);
    });
}