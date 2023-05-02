// For textarea tag
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
};
function OnInput(f) {
  this.style.height = 0;
  this.style.height = (this.scrollHeight) + "px";
};

// For settings button (menu burger icon)
let btn = document.querySelectorAll('#toggleTextarea');
btn.forEach(function (i) {
	i.addEventListener('click', function() {
		
		var elem = document.querySelector('.settings-bar');
		let marTop = getComputedStyle(elem).marginTop;

		if (marTop === "-156px") {
			elem.style.marginTop = "50px"
		} else if (marTop === "50px") {
			elem.style.marginTop = "-156px"
			setTimeout(function () { elem.style.marginTop = '-156px' });
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
function recordButtonFunc(i) {
	i.addEventListener('click', function() {
		let id = this.id
		let visibleDiv = i.parentElement.parentElement.id;
		document.getElementById(visibleDiv).style.display = 'none';
		if (visibleDiv === `half-${id}`) {
			document.getElementById(`full-${id}`).style.display = '';
		} else {
			document.getElementById(`half-${id}`).style.display = '';
		}
	});
};

// Animation for the post settings window
let threePoints = document.querySelectorAll('.three_points');
function threePointsFunc(i) {
	i.addEventListener('click', function() {

		var elem = this.nextElementSibling;

		if (elem) {
			
			if (elem.classList.contains('active')) {
				elem.style.height = getComputedStyle(elem).height;
				elem.classList.remove('active');
				getComputedStyle(elem).height; // reflow
				elem.style.height = '';
			} else {

			  	let record = this.closest('.record');
				let textArea = elem.getElementsByTagName('textarea')[0];

				if (!textArea.value) {
					let textList = record.getElementsByTagName('div');
					let string = '';

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
					string = string.trim()
					textArea.value = string;
					textArea.style.height = (textArea.scrollHeight) + "px";
				}

				elem.classList.add('active');
				var h = getComputedStyle(elem).height;
				elem.style.height = '0';
				getComputedStyle(elem).height; // reflow
				elem.style.height = h;
				setTimeout(function () { elem.style.height = '' }, 300);
		  	}
		}
	});
};


// AJAX delete record
let deleteRecordForms = document.querySelectorAll("#deleteRecord");
function deleteRecord(deleteRecordForm) {
	deleteRecordForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;

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
let createRecordForms = document.querySelectorAll("#createRecord");
createRecordForms.forEach(function (createRecordForm) {
	createRecordForm.addEventListener("submit", event => {
		event.preventDefault();

		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;
		let inputDiv = createRecordForm.getElementsByTagName('textarea')[0];
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
				inputDiv.style.height = 0 + "px";

				let blogsHome = document.getElementsByClassName('blog')[0];
				let firstChild = blogsHome.firstElementChild;

				let node = document.createElement("div");
				node.className = 'record';
				node.innerHTML += `<h6>${data.datetime}</h6>`

				if (text.length > 500) {
					node.innerHTML += `
					<div class="half-content" id="half-${data.id}">
						<div>
							<p>${text.substring(0,499)}...</p>
						</div>
						
						<div>
							<button id="${data.id}" href="javascript:void();" class="show-hide-btn">read more</button>
							<br/>
							<br/>
						</div>
					</div>
				
					<div class="full-content" id="full-${data.id}" style="display: none;">
						<div>
							<p>${text.replace('\n\n', '<br/><br/>')}</p>
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
						<input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
						<input id="delete_record" type="submit" value="Delete record">
					</form>
				</div>`;


				blogsHome.insertBefore(node, firstChild);

				threePointsFunc(node.getElementsByClassName('three_points')[0]);
				deleteRecord(node.querySelectorAll('#deleteRecord')[0]);

				if (text.length > 500) {
					let btns = node.querySelectorAll('.show-hide-btn');
					for (let i = 0; i < btns.length; i++) {
						recordButtonFunc(btns[i]);
					}
				}
			}
		})
	})
});


for (let i = 0; i < recordButton.length; i++) {
	recordButtonFunc(recordButton[i]);
}

for (let i = 0; i < threePoints.length; i++) {
	threePointsFunc(threePoints[i]);
}

for (let i = 0; i < deleteRecordForms.length; i++) {
	deleteRecord(deleteRecordForms[i]);
}
