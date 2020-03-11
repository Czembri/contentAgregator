const preload = document.querySelector('.preload');

preload.classList.add('show-preloader');
window.addEventListener('load', () => {
  	setTimeout(() => {
    	preload.classList.remove('show-preloader');
  	}, 1000);
});
