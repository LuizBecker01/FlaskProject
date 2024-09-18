class MobileNavbar{
  constructor(mobileManu, navList, navLink){
    this.mobileManu = document.querySelector(mobileManu);
    this.navList = document.querySelector(navList);
    this.navLink = document.querySelectorAll(navLink);
    this.activeClass = 'active';

    this.handleClick = this.handleClick.bind(); 
  }

  animateLinks(){
    this.navLink.forEach((link, index) => {
      link.style.animation
        ? (link.style.animation = "")
        : (link.style.animation = 'navLinkFade 0.5s ease forwards 0.3s');
    });
  }

  handleClick(){
    this.navList.classList.toggle(this.activeClass);
    this.mobileManu.classList.toggle(this.activeClass);
    this.animateLinks();
  }

  addClickEvent(){
    this.mobileManu.addEventListener('click', this.handleClick);
  }

  init(){
    if(this.mobileManu){
      this.addClickEvent();
    }
    return this;
  }
}

const mobileNavbar = new MobileNavbar(
  ".mobile-menu",
  ".nav-list",
  ".nav-list li",
);
mobileNavbar.init();

// Função para mostrar ou esconder o texto da sinopse
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

