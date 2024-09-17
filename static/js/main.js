const menuIcon = document.querySelector('nav .menu-ikona');
const mobileMenuItems = document.querySelector('nav .mobile-menu-elementi');

menuIcon.addEventListener('click', () => {
    mobileMenuItems.classList.toggle('active');
});