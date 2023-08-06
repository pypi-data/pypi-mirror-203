	// <![CDATA[  <-- For SVG support
window.addEventListener("DOMContentLoaded", (event) => {
	if ('WebSocket' in window) {
		(function () {
			var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
			var address = protocol + window.location.host + window.location.pathname + '/ws';
			var socket = new WebSocket(address);
			var task = 1;
			if (task === 1) {
				setTimeout(sendMessage, 100, socket);
			};
			console.log('Live reload enabled.');
			setInterval(sendMessage, 400, socket);
		})();
	}
	else {
		console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
};
})
	// ]]>

	// Server notifier about current page
function sendMessage(socket) {
	if (socket.readyState === 1) {
	socket.send("plserver");
	socket.onmessage = function (msg) {
		if (msg.data == 'reload') window.location.reload();
		};
	} else {
		var msg = "Has closed all connections."
		console.log("ws://" + window.location.host + window.location.pathname + '/ws ' + msg)
	}
}

function refreshCSS() {
	var sheets = [].slice.call(document.getElementsByTagName("link"));
	var head = document.getElementsByTagName("head")[0];
	for (var i = 0; i < sheets.length; ++i) {
		var elem = sheets[i];
		var parent = elem.parentElement || head;
		parent.removeChild(elem);
		var rel = elem.rel;
		if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
			var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
			elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
		}
		parent.appendChild(elem);
	}
}