function backgroundColorChange() {
	var color = window.getComputedStyle(document.body, null).getPropertyValue('background-color');

	if (color === "rgb(250, 244, 244)") {
		document.body.style.backgroundColor = "rgb(220, 244, 244)";
	} else if (color === "rgb(220, 244, 244)") {
		document.body.style.backgroundColor = "rgb(250, 244, 244)";
	};
};

let btns = document.querySelectorAll('#toggleTextarea');
btns.forEach(function (i) {
	i.addEventListener('click', function() {
	  let expanded = this.getAttribute('aria-expanded') === 'true' || false;
	  this.setAttribute('aria-expanded', !expanded);
	  let menu = this.nextElementSibling;
	  menu.hidden = !menu.hidden;
	});
});

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

const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}
function OnInput() {
  this.style.height = 0;
  this.style.height = (this.scrollHeight) + "px";
}