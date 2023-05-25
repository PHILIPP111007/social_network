const usernameInput = document.querySelector("#id_username");
const myDiv = usernameInput.parentElement;


function is_username_new(usernameInput) {
	usernameInput.addEventListener("input", event => {

		const val = usernameInput.value;

		if (val) {

			const url = `is_username_new/${val}`

			fetch(url, {
				method: 'GET',
				credentials: "same-origin",
				headers: {
				"X-Requested-With": "XMLHttpRequest",
				}
			})
			.then(response => response.json())
			.then(data => {

				if (myDiv.getElementsByTagName('p')[0]) {
					let p = myDiv.getElementsByTagName('p')[0];
					p.remove();
				}

				if (data.status) {
					myDiv.innerHTML += `<p style="padding:5px; color:white; background:green;">Nickname is free</p>`;
				} else {
					myDiv.innerHTML += `<p style="padding:5px; color:white; background:red;">This nickname is already taken</p>`;
				}

				usernameInput = document.querySelector("#id_username");
				usernameInput.value = val;
				usernameInput.focus();

				is_username_new(usernameInput);
			})
		} else {
			if (myDiv.getElementsByTagName('p')[0]) {
				let p = myDiv.getElementsByTagName('p')[0];
				p.remove();
			}
		}
	})
};

is_username_new(usernameInput);
