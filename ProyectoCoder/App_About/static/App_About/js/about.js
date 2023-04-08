/* Manejador de eventos para el botón */
const btn = document.querySelector('.btn');
btn.addEventListener('click', (event) => {
    event.preventDefault();
    window.location.href = "base" ;
});
