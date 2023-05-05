// Changing background color
let backgroundColorChange = document.querySelectorAll("#backgroundColorChangeForm");
backgroundColorChange.forEach(function (form) {
	form.addEventListener("submit", event => {
		event.preventDefault();

		var color = window.getComputedStyle(document.body, null).getPropertyValue('background-color');
		let csrftoken = event.srcElement.csrfmiddlewaretoken.value;
		let url = event.srcElement.action;
		let color_id = Number();

		if (color === "rgb(250, 244, 244)") {
			color_id = 0;
		} else if (color === "rgb(43, 43, 43)") {
			color_id = 1;
		};

		fetch(url, {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			"X-Requested-With": "XMLHttpRequest",
			"X-CSRFToken": csrftoken,
			},
			body: color_id
		})
		.then(response => response.json())
		.then(data => {
			if (data.status) {

				// dark theme
				if (color_id === 0) {
					document.body.style.backgroundColor = "rgb(43, 43, 43)";
					document.body.style.color = 'rgb(205, 205, 205)';

					let textarea = document.querySelectorAll('textarea')
					if (textarea) {
						textarea.forEach(function(i) {
							i.style.backgroundColor = 'rgb(68, 68, 75)'
							i.style.color = 'rgb(205, 205, 205)'
							i.style.borderColor = 'rgb(80, 80, 90)'
						})
					}

					let button = document.querySelectorAll('button')
					if (button) {
						button.forEach(function(i) {
							i.style.backgroundColor = 'rgb(101, 101, 110)'
							i.style.color = 'rgb(205, 205, 205)'
						})
					}

					let inputSubmit = document.querySelectorAll('input[type="submit"]')
					if (inputSubmit) {
						inputSubmit.forEach(function(i) {
							i.style.backgroundColor = 'rgb(101, 101, 110)'
							i.style.color = 'rgb(205, 205, 205)'
						})
					}

					let inputReset = document.querySelectorAll('input[type="reset"]')
					if (inputReset) {
						inputReset.forEach(function(i) {
							i.style.backgroundColor = 'rgb(101, 101, 110)'
							i.style.color = 'rgb(205, 205, 205)'
						})
					}

					let modal_txt = document.querySelectorAll('.modal_txt')
                    if (modal_txt) {
                        modal_txt.forEach(function(i) {
                            i.style.backgroundColor = 'rgb(57, 57, 61)'
                        })
                    }

					let inputText = document.querySelectorAll('input[type="text"]')
					if (inputText) {
						inputText.forEach(function(i) {
							i.style.backgroundColor = 'rgb(43, 43, 43)'
							i.style.color = 'rgb(205, 205, 205)'
						})
					}

					let inputEmail = document.querySelectorAll('input[type="email"]')
					if (inputEmail) {
						inputEmail.forEach(function(i) {
							i.style.backgroundColor = 'rgb(43, 43, 43)'
							i.style.color = 'rgb(205, 205, 205)'
						})
					}

					let menuLink_hover = document.querySelectorAll('.menu-link')
					for (let elem of menuLink_hover) {
						elem.addEventListener('mouseenter', () => {
						  elem.style.backgroundColor = 'rgb(49, 48, 57, 0.8)'
						})
						elem.addEventListener('mouseleave', () => {
						  elem.style.backgroundColor = ''
						})
					};

					let upper_line = document.querySelectorAll('.upper-line')[0]
					upper_line.style.backgroundColor = 'rgb(61, 61, 71, 0.8)'

					let settings_bar = document.querySelectorAll('.settings-bar')[0]
					settings_bar.style.backgroundColor = 'rgb(61, 61, 71, 0.8)'
					settings_bar.style.borderColor = 'rgb(80, 80, 90)'

					let left_list = document.querySelectorAll('.left-list')[0]
					left_list.style.backgroundColor = 'rgb(61, 61, 71, 0.8)'

					let user = document.querySelectorAll('.user')[0]
					if (user) {user.style.backgroundColor = 'rgb(57, 57, 61)'}

					let createRecord = document.querySelectorAll('#createRecord')[0]
					if (createRecord) {
						createRecord.style.backgroundColor = 'rgb(57, 57, 61)'
					}

					let record = document.querySelectorAll('.record')
					if (record) {
						record.forEach(function(i) {
							i.style.backgroundColor = 'rgb(57, 57, 61)'
						})
					}

					let delete_record = document.querySelectorAll('#delete_record')
					if (delete_record) {
						for (let elem of delete_record) {
							elem.addEventListener('mouseenter', () => {
							  elem.style.background = 'rgb(250, 135, 135)'
							  elem.style.color = '#c00f0fe2'
							})
							elem.addEventListener('mouseleave', () => {
								elem.style.background = ''
								elem.style.color = ''
							})
						};
					}

					let chat_href = document.querySelectorAll('.chat-href')
					if (chat_href) {
						chat_href.forEach(function(i) {
							i.style.backgroundColor = 'rgb(57, 57, 61)'
							i.style.color = 'rgb(205, 205, 205)'
						})

						for (let elem of chat_href) {
							elem.addEventListener('mouseenter', () => {
							  elem.style.backgroundColor = 'rgb(67, 67, 71)'
							})
							elem.addEventListener('mouseleave', () => {
							  elem.style.backgroundColor = 'rgb(57, 57, 61)'
							})
						};
					}

                    let find_form = document.querySelectorAll('.find-form')[0]
                    if (find_form) {find_form.style.backgroundColor = 'rgb(57, 57, 61)'}

					let user_card = document.querySelectorAll('.user-card')
                    if (user_card) {
                        user_card.forEach(function(i) {
                            i.style.backgroundColor = 'rgb(57, 57, 61)'
                            i.style.color = 'rgb(205, 205, 205)'
                        })
                    }

					let addButton = document.querySelectorAll('#addButton')
                    if (addButton) {
                        for (let elem of addButton) {
                            elem.addEventListener('mouseenter', () => {
                              elem.style.background = 'rgb(124, 234, 120)'
                              elem.style.color = 'rgb(54, 115, 52)'
                            })
                            elem.addEventListener('mouseleave', () => {
                                elem.style.background = 'rgb(101, 101, 110)'
                                elem.style.color = 'rgb(205, 205, 205)'
                            })
                        };
                    }

					let delButton = document.querySelectorAll('#delButton')
                    if (delButton) {
                        for (let elem of delButton) {
                            elem.addEventListener('mouseenter', () => {
                                  elem.style.background = 'rgb(250, 135, 135)'
                                elem.style.color = 'rgb(192, 15, 15)'
                            })
                            elem.addEventListener('mouseleave', () => {
                                elem.style.background = 'rgb(101, 101, 110)'
                                elem.style.color = 'rgb(205, 205, 205)'
                            })
                        };
                    }

				// light theme
				} else if (color_id === 1) {
					document.body.style.backgroundColor = "rgb(250, 244, 244)";
					document.body.style.color = 'rgb(0, 0, 0)'

					let textarea = document.querySelectorAll('textarea')
					if (textarea) {
						textarea.forEach(function(i) {
							i.style.backgroundColor = 'rgb(250, 244, 244)'
							i.style.color = 'rgb(0, 0, 0)'
							i.style.borderColor = 'rgb(80, 80, 90)'
						})
					}

					let button = document.querySelectorAll('button')
					if (button) {
						button.forEach(function(i) {
							i.style.backgroundColor = 'rgb(205, 205, 205)'
							i.style.color = '#2c2a2a'
						})
					}

					let inputSubmit = document.querySelectorAll('input[type="submit"]')
					if (inputSubmit) {
						inputSubmit.forEach(function(i) {
							i.style.backgroundColor = 'rgb(205, 205, 205)'
							i.style.color = '#2c2a2a'
						})
					}

					let inputReset = document.querySelectorAll('input[type="reset"]')
					if (inputReset) {
						inputReset.forEach(function(i) {
							i.style.backgroundColor = 'rgb(205, 205, 205)'
							i.style.color = '#2c2a2a'
						})
					}

					let modal_txt = document.querySelectorAll('.modal_txt')
					if (modal_txt) {
                        modal_txt.forEach(function(i) {
                            i.style.backgroundColor = 'rgb(250, 244, 244)'
                        })
                    }

					let inputText = document.querySelectorAll('input[type="text"]')
					if (inputText) {
						inputText.forEach(function(i) {
							i.style.backgroundColor = 'rgb(250, 244, 244)'
							i.style.color = '#2c2a2a'
						})
					}

					let inputEmail = document.querySelectorAll('input[type="email"]')
					if (inputEmail) {
						inputEmail.forEach(function(i) {
							i.style.backgroundColor = 'rgb(250, 244, 244)'
							i.style.color = '#2c2a2a'
						})
					}

					let menuLink_hover = document.querySelectorAll('.menu-link')
					for (let elem of menuLink_hover) {
						elem.addEventListener('mouseenter', () => {
						  elem.style.backgroundColor = 'rgb(220, 220, 220, 0.8)'
						})
						elem.addEventListener('mouseleave', () => {
						  elem.style.backgroundColor = ''
						})
					};

					let upper_line = document.querySelectorAll('.upper-line')[0]
					upper_line.style.backgroundColor = 'rgb(235, 235, 235, 0.8)'

					let settings_bar = document.querySelectorAll('.settings-bar')[0]
					settings_bar.style.backgroundColor = 'rgb(235, 235, 235, 0.8)'
					settings_bar.style.borderColor = '#cac3c3'

					let left_list = document.querySelectorAll('.left-list')[0]
					left_list.style.backgroundColor = 'rgb(235, 235, 235, 0.8)'

					let user = document.querySelectorAll('.user')[0]
					if (user) {user.style.backgroundColor = 'rgb(202, 195, 195)'}

					let createRecord = document.querySelectorAll('#createRecord')[0]
					if (createRecord) {
						createRecord.style.backgroundColor = 'rgb(202, 195, 195)'
					}

					let record = document.querySelectorAll('.record')
					if (record) {
						record.forEach(function(i) {
							i.style.backgroundColor = 'rgb(230, 230, 230, 0.73)'
						})
					}

					let delete_record = document.querySelectorAll('#delete_record')
					if (delete_record) {
						for (let elem of delete_record) {
							elem.addEventListener('mouseenter', () => {
							  elem.style.background = 'rgb(250, 135, 135)'
							  elem.style.color = 'rgb(192, 15, 15)'
							})
							elem.addEventListener('mouseleave', () => {
								elem.style.background = 'rgb(205, 205, 205)'
								elem.style.color = '#2c2a2a'
							})
						};
					}

					let chat_href = document.querySelectorAll('.chat-href')
					if (chat_href) {
						chat_href.forEach(function(i) {
							i.style.backgroundColor = 'rgb(250, 244, 244)'
							i.style.color = 'rgb(0, 0, 0)'
						})
	
						for (let elem of chat_href) {
							elem.addEventListener('mouseenter', () => {
							  elem.style.backgroundColor = 'rgb(227, 227, 227)'
							})
							elem.addEventListener('mouseleave', () => {
							  elem.style.backgroundColor = 'rgb(250, 244, 244)'
							})
						};
					}

                    let find_form = document.querySelectorAll('.find-form')[0]
                    if (find_form) {find_form.style.backgroundColor = 'rgb(202, 195, 195)'}

					let user_card = document.querySelectorAll('.user-card')
                    if (user_card) {
                        user_card.forEach(function(i) {
                            i.style.backgroundColor = 'rgb(230, 230, 230, 0.73)'
                            i.style.color = 'rgb(0, 0, 0)'
                        })
                    }

					let addButton = document.querySelectorAll('#addButton')
                    if (addButton) {
                        for (let elem of addButton) {
                            elem.addEventListener('mouseenter', () => {
                              elem.style.background = 'rgb(124, 234, 120)'
                              elem.style.color = 'rgb(54, 115, 52)'
                            })
                            elem.addEventListener('mouseleave', () => {
                                elem.style.background = 'rgb(205, 205, 205)'
                                elem.style.color = 'rgb(0, 0, 0)'
                            })
                        };
                    }

					let delButton = document.querySelectorAll('#delButton')
                    if (delButton) {
                        for (let elem of delButton) {
                            elem.addEventListener('mouseenter', () => {
                              elem.style.background = 'rgb(250, 135, 135)'
                                elem.style.color = 'rgb(192, 15, 15)'
                            })
                            elem.addEventListener('mouseleave', () => {
                                elem.style.background = 'rgb(205, 205, 205)'
                                elem.style.color = 'rgb(0, 0, 0)'
                            })
                        };
                    }
				};
			}
		})
	})
});
