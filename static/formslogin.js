const DaftarButton = document.getElementById('Daftar');
const MasukButton = document.getElementById('Masuk');
const container = document.getElementById('container');

DaftarButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

MasukButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});