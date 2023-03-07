// For textarea tag
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
};
function OnInput() {
  this.style.height = 0;
  this.style.height = (this.scrollHeight) + "px";
};


/*
// For settings button (menu burger icon)
let btns = document.querySelectorAll('#toggleTextarea');
btns.forEach(function (i) {
	i.addEventListener('click', function() {
	  let expanded = this.getAttribute('aria-expanded') === 'true' || false;
	  this.setAttribute('aria-expanded', !expanded);
	  let menu = this.nextElementSibling;
	  menu.hidden = !menu.hidden;
	});
});
*/

// For settings button (menu burger icon)
let btn = document.querySelectorAll('#toggleTextarea');
btn.forEach(function (i) {
	i.addEventListener('click', function() {
		
		var elem = document.querySelector('.settings-bar');
		let marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-134px") {
			elem.style.marginTop = "50px"
		} else if (marTop === "50px") {
			elem.style.marginTop = "-134px"
			setTimeout(function () { elem.style.marginTop = '-134px' }, 300);
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

// Animation for the post settings window
let threePoints = document.querySelectorAll('.three_points');
threePoints.forEach(function (i) {
	i.addEventListener('click', function() {

		var elem = this.nextElementSibling;

		if (elem) {
			
			if (elem.classList.contains('active')) {
			  elem.style.height = getComputedStyle(elem).height;
			  elem.classList.remove('active');
			  getComputedStyle(elem).height; // reflow
			  elem.style.height = '';
			} else {
			  elem.classList.add('active');
			  var h = getComputedStyle(elem).height;
			  elem.style.height = '0';
			  getComputedStyle(elem).height; // reflow
			  elem.style.height = h;
			  setTimeout(function () { elem.style.height = '' }, 300);
			}
		  }
	});
});
