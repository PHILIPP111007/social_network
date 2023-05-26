// insert youtube's iframe in post
function youTubeAPI(record) {
	
	const pattern = "https:\/\/youtu.be/([a-zA-Z0-9]+)";
	const dateTimeChild = record.firstElementChild;
	const post = dateTimeChild.nextElementSibling.textContent;
	const match = post.match(pattern);

	if (match) {

		const videoId = match[1];
		document.cookie = "witcher=Geralt; SameSite=None; Secure";
		const div = document.createElement('div');
		div.innerHTML = `
		<br/>
		<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/${videoId}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
		</iframe>`;
		record.append(div);
	}
};
