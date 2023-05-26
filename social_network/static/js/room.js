const body = document.getElementsByTagName('body')[0];
const tx = document.getElementsByTagName("textarea");
const modal = document.querySelector('#modal');


function lastMessageScroll(b) {
	const e = document.querySelector('.wrapper_Scrollbottom');
	if (e) {
		e.scrollIntoView({
			behavior: b || 'auto',
			block: 'end',
		});
	}
};

function copyText(msgId) {
	const text = document.getElementById(msgId).getElementsByTagName('div')[0].textContent;
	navigator.clipboard.writeText(text);
	messageInput.focus();
};

function showDeleteModal(msgId) {
	delMessageButton.name = msgId;
	modal.classList.add('modal_vis'); // добавляем видимость окна
	body.classList.add('body_block'); // убираем прокрутку
};

function hideDeleteModal() {
	modal.classList.remove('modal_vis');
	body.classList.remove('body_block');
	messageInput.focus();
};

// For input tag
for (let i = 0; i < tx.length; i++) {
	tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight));
	tx[i].addEventListener("input", OnInput, false);
};

function OnInput() {
	this.style.height = 0;
	this.style.height = this.scrollHeight + "px";
};


// Web Sockets
const roomName = JSON.parse(document.getElementById('room-name').textContent);
const globalUser = JSON.parse(document.getElementById('global-user').textContent);
const first_name = JSON.parse(document.getElementById('first_name').textContent);
const last_name = JSON.parse(document.getElementById('last_name').textContent);
const messageInput = document.querySelector("#id_message_send_input");
const sendButton = document.querySelector(".id_message_send_button");
const chatItemContainer = document.querySelector("#id_chat_item_container");
const delMessageButton = document.querySelector('.delMessageButton');
const chatSocket = new WebSocket(
	'ws://'
	+ window.location.host
	+ '/ws/chat/'
	+ roomName
	+ '/'
);
const deleteMessageSocket = new WebSocket(
	'ws://'
	+ window.location.host
	+ '/ws/delete_message/'
	+ roomName
	+ '/'
);


chatSocket.onopen = function (e) {
	console.log("chatSocket: The connection was setup successfully!");
	lastMessageScroll();
};

chatSocket.onclose = function (e) {
	console.error("chatSocket: Something unexpected happened!");
};

messageInput.focus();

messageInput.onkeyup = function (e) {
	if (e.keyCode == 13) {
		sendButton.click();
	}
};

sendButton.onclick = function (e) {
	const messageInputValue = messageInput.value.trim();
	messageInput.style.height = 0;
	messageInput.value = '';

	if (messageInputValue !== '') {
		chatSocket.send(JSON.stringify({
			message: messageInputValue,
			username: globalUser,
			first_name: first_name,
			last_name: last_name
		}));
	};
};

chatSocket.onmessage = function (e) {
	const data = JSON.parse(e.data);
	const text = linkify(data.message.trim().replace('\n', '\n<br/><br/>'));

	chatItemContainer.innerHTML += `
	<div id="${data.message_id}">
		<label>${data.first_name} ${data.last_name} ${data.timestamp}</label>
		<div id="${data.message_id}" class="text">${text}</div>

		<button class="hiddenButton" onclick="showDeleteModal(${data.message_id})">delete</button>
		<button class="hiddenButton" onclick="copyText(${data.message_id})">copy</button>
	</div>`;

	lastMessageScroll("smooth");
};


deleteMessageSocket.onopen = function (e) {
	console.log("deleteMessageSocket: The connection was setup successfully!");
};

deleteMessageSocket.onclose = function (e) {
	console.error("deleteMessageSocket: Something unexpected happened!");
};

delMessageButton.onclick = function (e) {
	deleteMessageSocket.send(JSON.stringify({
		pk: delMessageButton.name
	}))
};

deleteMessageSocket.onmessage = function (e) {
	const data = JSON.parse(e.data);
	hideDeleteModal();
	if (data.deleted) {
		document.getElementById(`${data.pk}`).remove();
	}
};
