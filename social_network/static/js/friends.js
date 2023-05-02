// For read-more / read-less buttons
let recordButton = document.querySelectorAll('.show-hide-btn');
recordButton.forEach(function (i) {
	i.addEventListener('click', function() {
		let id = this.id
		let visibleDiv = i.closest('div')?.id
		document.getElementById(visibleDiv).style.display = 'none';
		if (visibleDiv === `half-${id}`) {
			document.getElementById(`full-${id}`).style.display = '';
		} else {
			document.getElementById(`half-${id}`).style.display = '';
		}
	});
});


// AJAX add friend
let addFriendForms = document.querySelectorAll("#addFriendForm");
function addFriend(addFriendForm) {
	addFriendForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
		})
		.then(response => response.json())
		.then(data => {

			if (data.status) {

				// Удаление карточки подписчика

				let h_3_1 = document.getElementById('friends').getElementsByTagName('h3')[0];
				num = h_3_1.innerText.split(' ')[1];

				if (Number(num)) {
					num = Number(num) + 1;
				} else {
					num = 1;
					h_3_1.style = ''
				}
				text = `Friends: ${num}`;
				h_3_1.innerText = text;


				let h_3_2 = document.getElementById('subscribers').getElementsByTagName('h3')[0];
				num = h_3_2.innerText.split(' ')[1];
				num = Number(num);

				if (num === 1) {
					h_3_2.innerText = 'No subscribers';
					h_3_2.style = 'color:gray;';
				} else {
					num -= 1;
					h_3_2.innerText = `Subscribers: ${num}`;
				}

				addFriendForm.parentElement.remove();

				// Вставка этой карточки в новый div друзей
				let friendsHome = document.getElementById('friends');
				let h = friendsHome.getElementsByTagName('h3')[0].nextElementSibling;

				let placeholder = document.createElement("div");
				placeholder.innerHTML = `
				<div class="user-card">
					<a class="profile-link" href="/user/${data.username}/">
						<h4>${data.first_name} ${data.last_name}</h4>
						<h4 style="color:gray; font-size: 13px">@${data.username}</h4>
					</a>

					<form method="POST" action="make_chat/${data.username}/">
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input class="make_chat" type="submit" value="Chat">
					</form>

					<form id="deleteFriendForm" method="POST" action="delete_friend/${data.username}/">
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input id="delButton" class="delete_friend" type="submit" value="delete">
					</form>
				</div>`;
				let node = placeholder.firstElementChild;

				friendsHome.insertBefore(node, h);
				deleteFriend(node.getElementsByTagName('form')[1]);
			}
		})
	})
};


// AJAX delete friend
let deleteFriendForms = document.querySelectorAll("#deleteFriendForm");
function deleteFriend(deleteFriendForm) {
	deleteFriendForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
		})
		.then(response => response.json())
		.then(data => {

			if (data.status) {

				// Удаление карточки друга

				let h_3_1 = document.getElementById('subscribers').getElementsByTagName('h3')[0];
				num = h_3_1.innerText.split(' ')[1];

				if (Number(num)) {
					num = Number(num) + 1;
				} else {
					num = 1;
					h_3_1.style = ''
				}
				text = `Subscribers: ${num}`;
				h_3_1.innerText = text;


				let h_3_2 = document.getElementById('friends').getElementsByTagName('h3')[0];
				num = h_3_2.innerText.split(' ')[1];
				num = Number(num);

				if (num === 1) {
					h_3_2.innerText = 'No friends';
					h_3_2.style = 'color:gray;';
				} else {
					num -= 1;
					h_3_2.innerText = `Friends: ${num}`;
				}

				deleteFriendForm.parentElement.remove();

				// Вставка этой карточки в новый div подписчиков

				let subscribersHome = document.getElementById('subscribers');
				let h = subscribersHome.getElementsByTagName('h3')[0].nextElementSibling;

				let placeholder = document.createElement("div");
				placeholder.innerHTML = `
				<div class="user-card">
					<a class="profile-link" href="/user/${data.username}/">
						<h4>${data.first_name} ${data.last_name}</h4>
						<h4 style="color:gray; font-size: 13px">@${data.username}</h4>
					</a>

					<form method="POST" action="make_chat/${data.username}/">
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input class="make_chat" type="submit" value="Chat">
					</form>
					
					<form id="addFriendForm" method="POST" action="add_friend/${data.username}/" name="${data.username}">
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input id="addButton" class="add_friend" type="submit" value="add">
					</form>

					<form id="deleteSubscriberForm" method="POST" action="delete_subscriber/${data.username}/">
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input id="delButton" class="remove_subscribe" type="submit" value="delete">
					</form>
				</div>`;
				let node = placeholder.firstElementChild;

				subscribersHome.insertBefore(node, h);

				addFriend(node.getElementsByTagName('form')[1]);
				deleteSubscriber(node.getElementsByTagName('form')[2]);
			}
		})
	})
};


// AJAX delete subscription
let deleteSubscriptionForms = document.querySelectorAll("#deleteSubscriptionForm");
function deleteSubscription(deleteSubscriptionForm) {
	deleteSubscriptionForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
		})
		.then(response => response.json())
		.then(data => {

			if (data.status) {

				// Удаление карточки друга

				let h_3 = document.getElementById('subscriptions').getElementsByTagName('h3')[0];
				num = h_3.innerText.split(' ')[1];
				num = Number(num);

				if (num === 1) {
					h_3.innerText = 'No subscriptions';
					h_3.style = 'color:gray;';
				} else {
					num -= 1;
					h_3.innerText = `Subscriptions: ${num}`;
				}

				deleteSubscriptionForm.parentElement.remove();
			}
		})
	})
};


// AJAX add Subscription
let addSubscriptionForms = document.querySelectorAll("#addSubscriptionForm");
function addSubscription(addSubscriptionForm) {
	addSubscriptionForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
		})
		.then(response => response.json())
		.then(data => {

			if (data.status) {

				let h_3 = document.getElementById('subscriptions').getElementsByTagName('h3')[0];
				num = h_3.innerText.split(' ')[1];

				if (Number(num)) {
					num = Number(num) + 1;
				} else {
					num = 1;
					h_3.style = ''
				}
				text = `Subscriptions: ${num}`;
				h_3.innerText = text;

				addSubscriptionForm.parentElement.remove();

				// Вставка этой карточки в новый div подписок
				let subscriptionsHome = document.getElementById('subscriptions');

				let h = subscriptionsHome.getElementsByTagName('h3')[0].nextElementSibling;

				let placeholder = document.createElement("div");
				placeholder.innerHTML = `
				<div class="user-card">
					<a class="profile-link" href="/user/${data.username}/">
						<h4>${data.first_name} ${data.last_name}</h4>
						<h4 style="color:gray; font-size: 13px">@${data.username}</h4>
					</a>

					<form id="deleteSubscriptionForm" method="POST" action="delete_friend/${data.username}/">
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input id="delButton" class="remove_subscribe" type="submit" value="delete">
					</form>
				</div>`;
				let node = placeholder.firstElementChild;

				subscriptionsHome.insertBefore(node, h);
				deleteSubscription(node.getElementsByTagName('form')[0]);
			}
		})
	})
};


// AJAX delete Subscriber
let deleteSubscriberForms = document.querySelectorAll("#deleteSubscriberForm");
function deleteSubscriber(deleteSubscriberForm) {
	deleteSubscriberForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
		})
		.then(response => response.json())
		.then(data => {

			if (data.status) {

				// Удаление карточки подписчика

				let h_3 = document.getElementById('subscribers').getElementsByTagName('h3')[0];
				num = h_3.innerText.split(' ')[1];
				num = Number(num);

				if (num === 1) {
					h_3.innerText = 'No subscribers';
					h_3.style = 'color:gray;';
				} else {
					num -= 1;
					h_3.innerText = `Subscribers: ${num}`;
				}

				deleteSubscriberForm.parentElement.remove();
			}
		})
	})
};


for (let i = 0; i < deleteFriendForms.length; i++) {
	deleteFriend(deleteFriendForms[i]);
}

for (let i = 0; i < addFriendForms.length; i++) {
	addFriend(addFriendForms[i]);
}

for (let i = 0; i < deleteSubscriptionForms.length; i++) {
	deleteSubscription(deleteSubscriptionForms[i]);
}

for (let i = 0; i < addSubscriptionForms.length; i++) {
	addSubscription(addSubscriptionForms[i]);
}

for (let i = 0; i < deleteSubscriberForms.length; i++) {
	deleteSubscriber(deleteSubscriberForms[i]);
}
