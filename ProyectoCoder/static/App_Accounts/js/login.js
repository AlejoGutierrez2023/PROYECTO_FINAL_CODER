// Cambia el color de fondo del elemento con clase "background" cada 10 segundos
// setInterval(function() {
//     var colors = ['#ff4d4d', '#ffb84d', '#8cff4d', '#4dffc2', '#4d7aff', '#c04dff'];
//     var randomColor = colors[Math.floor(Math.random() * colors.length)];
//     document.querySelector('.background').style.backgroundColor = randomColor;
//     }, 3000);

setInterval(function() {
    var randomIndex = Math.floor(Math.random() * colors.length);
    form.style.backgroundColor = colors[randomIndex];
    }, 5000);
