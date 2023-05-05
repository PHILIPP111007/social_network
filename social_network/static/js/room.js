// For input tag
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
	tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight));
	tx[i].addEventListener("input", OnInput, false);
};
function OnInput(f) {
		this.style.height = 0;
		this.style.height = (this.scrollHeight) + "px";
};

function copyText(msgId) {
	text = document.getElementById(msgId).textContent;
	navigator.clipboard.writeText(text);
};
