// For settings button (menu burger icon)
let btn = document.querySelectorAll('#toggleTextarea');
btn.forEach(function (i) {
	i.addEventListener('click', function() {
		
		var elem = document.querySelector('.settings-bar');
		let marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-95px") {
			elem.style.marginTop = "50px"
		} else if (marTop === "50px") {
			elem.style.marginTop = "-95px"
			setTimeout(function () { elem.style.marginTop = '-95px' });
		};
	});
});

// Changing background color
let backgroundColorChange = document.querySelectorAll("#backgroundColorChangeForm");
backgroundColorChange.forEach(function (form) {
	form.addEventListener("submit", event => {
		event.preventDefault();

		var color = window.getComputedStyle(document.body, null).getPropertyValue('background-color');
		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;
		let color_id = Number();

		if (color === "rgb(250, 244, 244)") {
			color_id = 0;
		} else if (color === "rgb(220, 244, 244)") {
			color_id = 1;
		};

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
			body: color_id
		})
		.then(response => response.json())
		.then(data => {
			if (data.status) {

				if (color_id === 0) {
					document.body.style.backgroundColor = "rgb(220, 244, 244)";
				} else if (color_id === 1) {
					document.body.style.backgroundColor = "rgb(250, 244, 244)";
				};
			}
		})
	})
});
