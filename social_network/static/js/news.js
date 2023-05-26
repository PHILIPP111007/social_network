const blogDiv = document.querySelector('.blog');
const lazyDiv = document.querySelector('.lazyDiv');
const number = Number(JSON.parse(document.getElementById('posts_to_download').textContent));
const low_power_mode = JSON.parse(document.getElementById('low_power_mode').textContent);


// For read-more / read-less buttons
function recordButtonFunc(i) {
	i.addEventListener('click', function () {
		const id = this.id
		const visibleDiv = i.parentElement.parentElement.id;
		document.getElementById(visibleDiv).style.display = 'none';
		if (visibleDiv === `half-${id}`) {
			document.getElementById(`full-${id}`).style.display = '';
		} else {
			document.getElementById(`half-${id}`).style.display = '';
		}
	});
};


// lazy download posts
const observer = new IntersectionObserver((entries) => {
	if (entries[0].isIntersecting) {

		const posts_number = Number(lazyDiv.id);
		const url = `lazy_loader/${posts_number}`;

		if (blogDiv.innerHTML === "") {
			blogDiv.innerHTML = "<h4>Wait...</h4>";
		}

		fetch(url, {
			method: 'GET',
			credentials: "same-origin",
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			}
		})
			.then(response => response.json())
			.then(data => {
				if (data.status) {

					if (blogDiv.innerHTML === "<h4>Wait...</h4>") {
						blogDiv.innerHTML = "";
					}

					lazyDiv.id = posts_number + number;

					const posts = data.friends_records;

					for (let i = 0; i < posts.length; i++) {

						const node = document.createElement("div");
						node.className = 'record';

						if (posts[i].is_changed) {
							node.innerHTML += `
							<a class="profile-link" href="/user/${posts[i].user_id}/">
								<h3>${posts[i].first_name} ${posts[i].last_name}</h3>
								<h6>@${posts[i].user_id}</h6>
								<h6>${posts[i].date_time} Modified</h6>
							</a>`;
						} else {
							node.innerHTML += `
							<a class="profile-link" href="/user/${posts[i].user_id}/">
								<h3>${posts[i].first_name} ${posts[i].last_name}</h3>
								<h6>@${posts[i].user_id}</h6>
								<h6>${posts[i].date_time}</h6>
							</a>`;
						}

						const text = linkify(posts[i].content.replace('\n', '\n<br/><br/>'));

						if (text.length > 500) {

							const halfText = text.substring(0,499);

							node.innerHTML += `
							<div class="half-content" id="half-${posts[i].id}">
								<div>
									<p>${halfText}...</p>
								</div>
								
								<div>
									<button id="${posts[i].id}" href="javascript:void();" class="show-hide-btn">read more</button>
									<br/>
									<br/>
								</div>
							</div>
						
							<div class="full-content" id="full-${posts[i].id}" style="display: none;">
								<div>
									<p>${text}</p>
								</div>
								
								<div>
									<button id="${posts[i].id}" class="show-hide-btn">read less</button>
									<br/>
									<br/>
								</div>
							</div>`;
						} else {
							node.innerHTML += `<div><p>${text}</p></div>`;
						}

						if (posts[i].content.length > 500) {
							const btns = node.querySelectorAll('.show-hide-btn');
							for (let i = 0; i < btns.length; i++) {
								recordButtonFunc(btns[i]);
							}
						}

						if (low_power_mode) {
							youTubeAPI(node);
						}

						blogDiv.appendChild(node);
					}
				} else {
					if (blogDiv.innerHTML === "<h4>Wait...</h4>") {
						blogDiv.innerHTML = "";
					}
				}
			})
	}
});

observer.observe(lazyDiv);
