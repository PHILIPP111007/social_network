// For settings button (menu burger icon)
const btn = document.querySelectorAll('#toggleTextarea');
btn.forEach(function (i) {
	i.addEventListener('click', function() {
		
		var elem = document.querySelector('.settings-bar');
		const marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-95px") {
			elem.style.marginTop = "50px"
		} else if (marTop === "50px") {
			elem.style.marginTop = "-95px"
			setTimeout(function () { elem.style.marginTop = '-95px' });
		};
	});
});
