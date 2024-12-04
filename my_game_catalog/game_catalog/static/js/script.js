// Script para adicionar um efeito de hover nos itens da lista de jogos
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona um efeito de "hover" para os itens de jogo
    const jogos = document.querySelectorAll('.jogo-item');
    
    jogos.forEach(function(jogo) {
        jogo.addEventListener('mouseenter', function() {
            jogo.style.transform = 'scale(1.05)';
        });

        jogo.addEventListener('mouseleave', function() {
            jogo.style.transform = 'scale(1)';
        });
    });
});

// Validação de formulário - Exemplo de como validar o campo de nome do jogo
function validarFormulario() {
    const nomeJogo = document.getElementById('id_nome');
    if (nomeJogo.value.trim() === '') {
        alert('O nome do jogo é obrigatório!');
        return false;
    }
    return true;
}

// Exemplo de adicionar uma classe de "loading" enquanto um formulário está sendo enviado
document.querySelector('form').addEventListener('submit', function(e) {
    const loadingMessage = document.createElement('div');
    loadingMessage.textContent = 'Enviando...';
    loadingMessage.classList.add('loading-message');
    document.body.appendChild(loadingMessage);
    setTimeout(function() {
        // Simulação de envio de formulário
        alert('Formulário enviado!');
        // Aqui você pode adicionar a lógica real de envio de formulário, como um fetch ou AJAX.
    }, 2000);  // Simulando um tempo de envio de 2 segundos
});
