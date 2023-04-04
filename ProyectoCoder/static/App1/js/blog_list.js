// Agregar evento click a los enlaces de detalle de blog
const blogDetailLinks = document.querySelectorAll('.blog-list-link');
blogDetailLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        const pk = this.dataset.pk;
        // Hacer una petición AJAX para obtener los detalles del blog
        fetch(`/blogs/${pk}/`)
        .then(response => response.json())
        .then(data => {
            // Mostrar los detalles del blog en un modal
            const modal = document.createElement('div');
            modal.classList.add('modal');
            modal.innerHTML = `
                <div class="modal-content">
                    <span class="close">&times;</span>
                    <h2>${data.title}</h2>
                    <p>${data.subtitle}</p>
                    <img src="${data.image}" alt="${data.title}">
                    <p>${data.body}</p>
                    <p>Author: ${data.author}</p>
                    <p>Date: ${data.created_at}</p>
                </div>
            `;
            document.body.appendChild(modal);
            // Agregar evento click al botón de cerrar modal
            const closeButton = modal.querySelector('.close');
            closeButton.addEventListener('click', function() {
                modal.remove();
            });
        })
        .catch(error => console.log(error));
    });
});
