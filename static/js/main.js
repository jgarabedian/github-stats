// Animate scrolling

$(document).ready(function(){  
  $("#repo-nav").click(function(e) {
    e.preventDefault();
    $([document.documentElement, document.body]).animate({
      scrollTop: $('#repo-header').offset().top
    }, 1500);
  });
});

$(document).ready(function(){  
  $("#back-to-top").click(function(e) {
    e.preventDefault();
    $([document.documentElement, document.body]).animate({
      scrollTop: 0
  	}, 1500);
  });
});
