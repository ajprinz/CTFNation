function getParameterByName(name, url) {
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

$(document).ready(function () {
    var game = getParameterByName('game');

    if(game != undefined && game != null) {
        // Note that the path doesn't matter right now; any WebSocket
        // connection gets bumped over to WebSocket consumers
        socket = new WebSocket("ws://" + window.location.host + "/" + game);

        socket.onmessage = function (e) {
            $('#message-container').append('<div>' + e.data + '</div>');
        };

        socket.onopen = function () {
            socket.send("a new user wants to play " + game);
        };

        // Call onopen directly if socket is already open
        if (socket.readyState == WebSocket.OPEN) socket.onopen();
    } else {
        $('#game-name').html('Please select a game by adding querystring ?game=you_room_of_choice');
    }
});
