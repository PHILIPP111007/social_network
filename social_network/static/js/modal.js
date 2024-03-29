const body = document.getElementsByTagName('body')[0];
const openModalButton = document.querySelectorAll('.open_modal');
const closeModalButton = document.querySelectorAll('.close_modal');
let modal;

openModalButton.forEach(function (i) {
	i.addEventListener('click', function() {
		modal = document.getElementById(`modal_${this.id}`);
		modal.classList.add('modal_vis'); // добавляем видимость окна
		body.classList.add('body_block'); // убираем прокрутку
	});
});

closeModalButton.forEach(function (i) {
	i.addEventListener('click', function() {
		modal.classList.remove('modal_vis');
		body.classList.remove('body_block');
	});
});
