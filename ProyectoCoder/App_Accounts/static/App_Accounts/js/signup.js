// static/js/register.js
// Código JavaScript para el formulario de registro
document.addEventListener("DOMContentLoaded", function() {
    let inputs = document.querySelectorAll("input");
    if (inputs) {
        inputs.forEach(input => {
            input.addEventListener("focus", function() {
                let helpText = this.nextElementSibling;
                if (helpText) {
                    helpText.style.display = "none";
                }
            });
            input.addEventListener("blur", function() {
                let helpText = this.nextElementSibling;
                if (helpText) {
                    helpText.style.display = "block";
                }
            });
        });
    }
});
// Selecciona el elemento con la clase "form"
var form = document.querySelector('.form');

// Define una lista de colores



// Establece un temporizador para cambiar el color de fondo cada 5 segundos
setInterval(function() {
  var randomIndex = Math.floor(Math.random() * colors.length);
form.style.backgroundColor = colors[randomIndex];
}, 5000); // 5000 milisegundos = 5 segundos

