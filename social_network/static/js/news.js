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
