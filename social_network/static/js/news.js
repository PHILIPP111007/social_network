// For read-more / read-less buttons
const recordButton = document.querySelectorAll('.show-hide-btn');
recordButton.forEach(function (i) {
	i.addEventListener('click', function() {
		const id = this.id
		const visibleDiv = i.closest('div')?.id
		document.getElementById(visibleDiv).style.display = 'none';
		if (visibleDiv === `half-${id}`) {
			document.getElementById(`full-${id}`).style.display = '';
		} else {
			document.getElementById(`half-${id}`).style.display = '';
		}
	});
});
