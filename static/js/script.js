$(document).ready(function(){


var origOffsetY = 700;

function scroll () {
if ($(window).scrollTop() >= origOffsetY) {
$('nav.nav-panel').addClass('sticky');
} else {
$('nav.nav-panel').removeClass('sticky');
} 


}

document.onscroll = scroll;

});