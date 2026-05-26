document.getElementById('csv').onchange = function() {
    if (this.files && this.files.length > 0) {
        const arquivoNome = this.files[0].name;
        
        document.querySelector('.uploader span').innerText = `Arquivo ${arquivoNome}`;
        document.querySelector('.uploader').style.borderColor = "#28a745";
        document.querySelector('.uploader').style.background = "#e8f5e9";
        document.querySelector('.uploader i').className = "fa-solid fa-circle-check";
        document.querySelector('.uploader i').style.color = "#28a745";
    }
};

const form = document.querySelector('form');
form.onsubmit = function(e) {
    const input = document.getElementById('csv');
    
   //input vazio
    if (!input.files || input.files.length === 0) {
        e.preventDefault(); // Bloqueia o envio
        alert('É necessário enviar um arquivo .CSV para criar o relatório');
        return false;
    }
    
    // não CSV
    const arquivoNome = input.files[0].name;
    if (!arquivoNome.toLowerCase().endsWith('.csv')) {
        e.preventDefault(); // Bloqueia o envio
        alert('Por favor, envie um arquivo com a extensão .CSV');
        return false;
    }
};