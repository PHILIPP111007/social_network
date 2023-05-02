// AJAX delete Subscriber
let usernameInput = document.querySelector("#id_username");

function is_username_new(usernameInput) {
	usernameInput.addEventListener("input", event => {

        val = usernameInput.value;

        if (val) {

            url = `is_username_new/${val}`

            fetch(url, {
                method: 'GET',
                credentials: "same-origin",
                headers: {
                "X-Requested-With": "XMLHttpRequest",
                }
            })
            .then(response => response.json())
            .then(data => {

                myDiv = usernameInput.parentElement;
                if (myDiv.getElementsByTagName('p')[0]) {
                    p = myDiv.getElementsByTagName('p')[0];
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
            myDiv = usernameInput.parentElement;
            if (myDiv.getElementsByTagName('p')[0]) {
                p = myDiv.getElementsByTagName('p')[0];
                p.remove();
            }
        }
    })
};

is_username_new(usernameInput);
