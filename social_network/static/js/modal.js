let openModalButton = document.querySelectorAll('.open_modal');
let closeModalButton = document.querySelectorAll('.close_modal');
let body = document.getElementsByTagName('body')[0];
let modal = ''

openModalButton.forEach(function (i) {
    i.addEventListener('click', function() {

        modal = document.getElementById(`modal_${this.id}`);

        modal.classList.add('modal_vis'); // добавляем видимость окна
        modal.classList.remove('bounceOutDown'); // удаляем эффект закрытия
        body.classList.add('body_block'); // убираем прокрутку
	});
});

closeModalButton.forEach(function (i) {
    i.addEventListener('click', function() {
        modal.classList.add('bounceOutDown'); // добавляем эффект закрытия
        modal.classList.remove('modal_vis');
        body.classList.remove('body_block');
	});
});
