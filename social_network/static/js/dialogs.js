// For settings button (menu burger icon)
let btn = document.querySelectorAll('#toggleTextarea');
btn.forEach(function (i) {
	i.addEventListener('click', function() {
		
		var elem = document.querySelector('.settings-bar');
		let marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-77px") {
			elem.style.marginTop = "50px"
		} else if (marTop === "50px") {
			elem.style.marginTop = "-77px"
			setTimeout(function () { elem.style.marginTop = '-77px' }, 300);
		};
	});
});

// Changing background color
// (but now this style does not affect other pages and is not saved)
function backgroundColorChange() {
	var color = window.getComputedStyle(document.body, null).getPropertyValue('background-color');

	if (color === "rgb(250, 244, 244)") {
		document.body.style.backgroundColor = "rgb(220, 244, 244)";
	} else if (color === "rgb(220, 244, 244)") {
		document.body.style.backgroundColor = "rgb(250, 244, 244)";
	};
};

let button = document.querySelectorAll('#room-name-button');
button.forEach(function (i) {
	i.addEventListener('click', function() {
		const username = i.textContent
		var roomName = i.value;
		window.location.pathname = `/social_network/dialogs/${username}/chat/${roomName}/`;
	});
})