var carousel = document.querySelector('.carousel');
var slides = carousel.querySelectorAll('.carousel-slide');
var currentIndex = 0;
var interval = setInterval(nextSlide, 3000); // автоматическая прокрутка каждые 3 секунды

function nextSlide() {
  slides[currentIndex].classList.remove('active');
  currentIndex = (currentIndex + 1) % slides.length;
  slides[currentIndex].classList.add('active');
}