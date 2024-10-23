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
          : (link.style.animation = 'navLinkFade 0.5s ease forwards');
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
  