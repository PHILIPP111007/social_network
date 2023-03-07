// For settings button (menu burger icon)
let btn = document.querySelectorAll('#toggleTextarea');
btn.forEach(function (i) {
	i.addEventListener('click', function() {
		
		var elem = this.nextElementSibling;
		let marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-108px") {
			elem.style.marginTop = "10px"
		} else if (marTop === "10px") {
			elem.style.marginTop = "-108px"
			setTimeout(function () { elem.style.marginTop = '-108px' }, 300);
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
