document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');
  header.className = header.classList.contains('red') ? 'green' : 'red';
});
