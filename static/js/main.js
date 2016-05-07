/**
 * Send an Ajax request to open the door.
 */
function open(email, password) {
    var xhr = new XMLHttpRequest();

    var data = new FormData();
    data.append('email', email);
    data.append('password', password);

    xhr.open('POST', window.location, true);
    xhr.onload = function() {
        if (xhr.status == 401) {
            alert('Falsche Zugangsdaten!');
        } else if (xhr.status != 204) {
            alert('Serverfehler');
        }
    };
    xhr.onerror = function() {
        alert('Verbindungsfehler');
    };

    alert('Die Türe sollte nun für einige Sekunden geöffnet sein...');
    xhr.send(data);
}

/**
 * Execute function `fn` once `DOMContentLoaded` fires.
 */
function ready(fn) {
    if (document.readyState != 'loading'){
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}

/**
 * Add event listeners to DOM.
 */
ready(function() {
    var button = document.getElementById('opendoor');
    button.addEventListener('submit', function(event) {
        event.preventDefault();
        var email = this.querySelector('#email').value;
        var password = this.querySelector('#password').value;
        open(email, password);
        return false;
    });
});
