function toggleText(card) {
    // Seleciona a div com a classe 'hidden' dentro do card clicado
    const moreText = card.querySelector('.hidden');
  
    // Oculta todas as outras sinopses
    const allText = document.querySelectorAll('.card .hidden');
    allText.forEach((text) => {
      if (text !== moreText) {
        text.style.display = 'none';
      }
    });
  
    // Alterna entre mostrar ou esconder o texto da sinopse clicada
    if (moreText.style.display === 'block') {
      moreText.style.display = 'none';
    } else {
      moreText.style.display = 'block';
    }
}