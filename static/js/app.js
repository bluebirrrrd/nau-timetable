function main(event) {
	var header = document.querySelector('header');
	var stickyNav = document.querySelector('nav.nav-panel');

	var scrollHandler = function(e) {
		var scrollPos = window.pageYOffset || document.documentElement.scrollTop;
		var stickyLine = header.scrollHeight - stickyNav.scrollHeight;
		if (scrollPos > stickyLine) {
			stickyNav.classList.add('sticky');
		} else if (stickyNav.classList.contains('sticky')) {
			stickyNav.classList.remove('sticky');
		}
	};

	window.addEventListener('scroll', scrollHandler);
}

document.addEventListener('DOMContentLoaded', main);