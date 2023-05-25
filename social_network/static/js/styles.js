// Changing system theme
const backgroundColorChange = document.querySelectorAll("#backgroundColorChangeForm");
backgroundColorChange.forEach(function (form) {
	form.addEventListener("submit", event => {
		event.preventDefault();

		const csrftoken = window.CSRF_TOKEN;
		const url = event.srcElement.action;
		const color = window.getComputedStyle(document.body, null).getPropertyValue('background-color');
		let color_id;

		if (color === "rgb(250, 244, 244)") {
			color_id = 0;
		} else if (color === "rgb(43, 43, 43)") {
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
					document.querySelector("body").className = "body-dark";
				} else if (color_id === 1) {
					document.querySelector("body").className = "body-light";
				};
			}
		})
	})
});
