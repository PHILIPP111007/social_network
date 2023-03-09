// insert youtube's iframe in post
var records = document.querySelectorAll('.record');
let pattern = "https:\/\/youtu.be/([a-zA-Z0-9]+)";

records.forEach(function(record) {
	
	var dateTimeChild = record.firstElementChild
	var post = dateTimeChild.nextElementSibling.textContent
	var match = post.match(pattern)

	if (match) {

		var videoId = match[1]

		let div = document.createElement('div');
		div.innerHTML = `<br/><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/${videoId}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>`;
		record.append(div);
	}
});
