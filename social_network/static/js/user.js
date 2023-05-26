const csrftoken = window.CSRF_TOKEN;
const textArea = document.getElementsByTagName("textarea")[0];
const menuButton = document.querySelector('#toggleTextarea');
const createRecordForm = document.querySelector("#createRecord");
const blogDiv = document.querySelector('.blog');
const lazyDiv = document.querySelector('.lazyDiv');
const number = Number(JSON.parse(document.getElementById('posts_to_download').textContent));
const is_my_page = JSON.parse(document.getElementById('is_my_page').textContent);
const low_power_mode = JSON.parse(document.getElementById('low_power_mode').textContent);


function OnInput() {
	this.style.height = 0;
	this.style.height = this.scrollHeight + "px";
};


// For textarea tag
function textareaScroll(textArea) {
	textArea.setAttribute("style", "height:" + (textArea.scrollHeight));
	textArea.addEventListener("input", OnInput, false);
};


// For settings button (menu burger icon)
function settingsButton(i) {
	i.addEventListener('click', function() {
		
		const elem = document.querySelector('.settings-bar');
		const marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-190px") {
			elem.style.marginTop = "50px"
		} else if (marTop === "50px") {
			elem.style.marginTop = "-190px"
			setTimeout(function () { elem.style.marginTop = '-190px' });
		};
	});
};


// For read-more / read-less buttons
function recordButtonFunc(i) {
	i.addEventListener('click', function() {
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


// Animation for the post settings window
function threePointsFunc(i) {
	i.addEventListener('click', function() {

		const elem = this.nextElementSibling;

		if (elem) {
			
			if (elem.classList.contains('active')) {
				elem.style.height = getComputedStyle(elem).height;
				elem.classList.remove('active');
				getComputedStyle(elem).height; // reflow
				elem.style.height = '';
			} else {

			  	const record = this.closest('.record');
				const textArea = elem.getElementsByTagName('textarea')[0];

				if (!textArea.value) {
					const textList = record.getElementsByTagName('div');
					let string = '';
					let text;

					if (textList.length === 4 | textList.length === 5) {
						text = textList[0];
					} else if (textList.length === 9 | textList.length === 10) {
						text = textList[3];
						text = text.getElementsByTagName('div')[0];
					}

					text = text.getElementsByTagName('p');

					for (let i = 0; i < text.length; i++) {
						string += text[i].textContent + '\n\n';
					}
					string = string.trim();
					textArea.value = string;
					textArea.style.height = (textArea.scrollHeight) + "px";
				}

				elem.classList.add('active');
				const h = getComputedStyle(elem).height;
				elem.style.height = '0';
				getComputedStyle(elem).height; // reflow
				elem.style.height = h;
				setTimeout(function () { elem.style.height = '' }, 300);
		  	}
		}
	});
};


// AJAX delete record
function deleteRecord(deleteRecordForm) {
	deleteRecordForm.addEventListener("submit", event => {
		event.preventDefault();

		const url = event.srcElement.action;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
		})
		.then(response => response.json())
		.then(data => {
			if (data.status) {
				deleteRecordForm.parentElement.parentElement.remove();
			}
		})
	})
};


// AJAX create record
function createRecord(createRecordForm) {
	createRecordForm.addEventListener("submit", event => {
		event.preventDefault();

		const url = event.srcElement.action;
		const inputDiv = createRecordForm.getElementsByTagName('textarea')[0];
		let text = inputDiv.value;

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
			body: text
		})
		.then(response => response.json())
		.then(data => {
			if (data.status) {

				inputDiv.value = '';
				inputDiv.style.height = 0;

				const blogsHome = document.getElementsByClassName('blog')[0];
				const firstChild = blogsHome.firstElementChild;

				const node = document.createElement("div");
				node.className = 'record';
				node.innerHTML += `<h6>${data.datetime}</h6>`

				if (text.length > 500) {
					node.innerHTML += `
					<div class="half-content" id="half-${data.id}">
						<div>
							<p>${text.substring(0,499).replace('\n\n', '\n\n<br/><br/>')}...</p>
						</div>
						
						<div>
							<button id="${data.id}" href="javascript:void();" class="show-hide-btn">read more</button>
							<br/>
							<br/>
						</div>
					</div>
				
					<div class="full-content" id="full-${data.id}" style="display: none;">
						<div>
							<p>${text.replace('\n\n', '\n\n<br/><br/>')}</p>
						</div>
						
						<div>
							<button id="${data.id}" class="show-hide-btn">read less</button>
							<br/>
							<br/>
						</div>
					</div>`;


				} else {
					node.innerHTML += `<div><p>${text}</p></div>`;
				}

				node.innerHTML += `
				<img class="three_points" src="/static/images/three_points.svg" width="20" height="20" alt="three points">

				<div class="record-bar">
					<div id="change-record">
						<div>
							<form method="POST" action="change_record/${data.id}/">
								<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
								<textarea name="my_textarea" maxlength="5000" placeholder="Edit record"></textarea>
								<input type="submit" name="edit" value="Edit record">
							</form>
						</div>
					</div>
					<form id="deleteRecord" method="POST" action="delete_record/${data.id}/">
						<input id="delete_record" type="submit" value="Delete record">
					</form>
				</div>`;

				blogsHome.insertBefore(node, firstChild);

				nodeAddListeners(node);

				if (text.length > 500) {
					const btns = node.querySelectorAll('.show-hide-btn');
					for (let i = 0; i < btns.length; i++) {
						recordButtonFunc(btns[i]);
					}
				}
			}
		})
	})
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

					const posts = data.blog;

					for (let i = 0; i < posts.length; i++) {

						const node = document.createElement("div");
						node.className = 'record';

						if (posts[i].is_changed) {
							node.innerHTML += `<h6>${posts[i].date_time} Modified</h6>`;
						} else {
							node.innerHTML += `<h6>${posts[i].date_time}</h6>`;
						}

						if (posts[i].content.length > 500) {
							node.innerHTML += `
							<div class="half-content" id="half-${posts[i].id}">
								<div>
									<p>${posts[i].content.substring(0,499).replace('\n\n', '\n\n<br/><br/>')}...</p>
								</div>
								
								<div>
									<button id="${posts[i].id}" href="javascript:void();" class="show-hide-btn">read more</button>
									<br/>
									<br/>
								</div>
							</div>
						
							<div class="full-content" id="full-${posts[i].id}" style="display: none;">
								<div>
									<p>${posts[i].content.replace('\n\n', '\n\n<br/><br/>')}</p>
								</div>
								
								<div>
									<button id="${posts[i].id}" class="show-hide-btn">read less</button>
									<br/>
									<br/>
								</div>
							</div>`;
						} else {
							node.innerHTML += `<div><p>${posts[i].content.replace('\n\n', '\n\n<br/><br/>')}</p></div>`;
						}

						if (is_my_page) {
							node.innerHTML += `
							<img class="three_points" src="/static/images/three_points.svg" width="20" height="20" alt="three points">

							<div class="record-bar">
								<div id="change-record">
									<div>
										<form method="POST" action="change_record/${posts[i].id}/">
											<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
											<textarea name="my_textarea" maxlength="5000" placeholder="Edit record"></textarea>
											<input type="submit" name="edit" value="Edit record">
										</form>
									</div>
								</div>
								<form id="deleteRecord" method="POST" action="delete_record/${posts[i].id}/">
									<input id="delete_record" type="submit" value="Delete record">
								</form>
							</div>`;
						}

						if (is_my_page) {
							nodeAddListeners(node);
						}

						if (posts[i].content.length > 500) {
							const btns = node.querySelectorAll('.show-hide-btn');
							for (let i = 0; i < btns.length; i++) {
								recordButtonFunc(btns[i]);
							}
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


function nodeAddListeners(node) {
	threePointsFunc(node.getElementsByClassName('three_points')[0]);
	textareaScroll(node.getElementsByTagName("textarea")[0]);
	deleteRecord(node.querySelectorAll('#deleteRecord')[0]);

	if (low_power_mode) {
		youTubeAPI(node);
	}
};


settingsButton(menuButton);
if (is_my_page) {
	textareaScroll(textArea);
	createRecord(createRecordForm);
}
if (lazyDiv) {
	observer.observe(lazyDiv);
}
