
    document.addEventListener('DOMContentLoaded', function() {
    // Script para mostrar/ocultar cuerpo de mensajes al hacer clic en botón
    const btnsToggleMessageBody = document.querySelectorAll('[id^="btn-toggle-message-body-"]');
    btnsToggleMessageBody.forEach(btn => {
        btn.addEventListener('click', function() {
            const messageBody = this.nextElementSibling;
            if (messageBody) {
                messageBody.classList.toggle('expanded');
                this.textContent = messageBody.classList.contains('expanded') ? 'Ocultar mensaje' : 'Mostrar mensaje';
            }
        });
    });
});