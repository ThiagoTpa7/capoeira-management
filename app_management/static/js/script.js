document.addEventListener("DOMContentLoaded", () => {

    const botoes = document.querySelectorAll('.efeito-btn');

    botoes.forEach(botao => {

        botao.addEventListener('mouseenter', () => {
            botao.style.boxShadow = "0 8px 20px rgba(0,0,0,0.2)";
        });

        botao.addEventListener('mouseleave', () => {
            botao.style.boxShadow = "none";
        });

    });

});

document.querySelectorAll('.efeito-btn').forEach(botao => {

    botao.addEventListener('click', function(e) {

        const ripple = document.createElement('span');

        ripple.classList.add('ripple');

        this.appendChild(ripple);

        const x = e.clientX - e.target.offsetLeft;
        const y = e.clientY - e.target.offsetTop;

        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;

        setTimeout(() => {
            ripple.remove();
        }, 600);

    });

});