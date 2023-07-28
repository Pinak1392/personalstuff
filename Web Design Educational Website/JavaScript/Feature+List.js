$(function(){
  //width is 100%
  var wid = '100%';
  //speed 1 secs to move
  var anim = 1500;
  //Pause 5 secs
  var Inter = 5000;
  //Current slide
  var curSlide = 1;
  //Amount of slides we have
  var slideLen = $('#slider').find('.slides').find('.slide').length

  var pause;
  $('.' + String(curSlide) + ' > a > h3').fadeIn('slow');

  function startSlide (){
    pause = setInterval(function() {
      $('.' + String(curSlide) + ' > a > h3').fadeOut();
      $('#slider .slides').animate({'margin-left':'-=' + wid}, anim, function(){
        //Move slide so we on a slide higher
        curSlide++;
        $('.' + String(curSlide) + ' > a > h3').fadeIn('slow');
        if (curSlide === slideLen) {
          $('.' + String(curSlide) + ' > a > h3').css('display', 'none');
          curSlide = 1;
          $('.slides').css('margin-left', '0%');
          $('.' + String(curSlide) + ' > a > h3').fadeIn('slow');
        }
      });
    }, Inter);
  }

  function stopSlide (){
    clearInterval(pause);
  }

  startSlide()
  $('#slider').on('mouseenter', stopSlide).on('mouseleave', startSlide);
});

function slidedown(element, i){
  if ($('.' + i).css('display') === 'none'){
    $(element).css('border-radius', '10px 10px 0px 0px');
    $(element).css('margin-bottom', '2%');
    $('.' + i).slideDown();
  } else {
    $(element).css('border-radius', '0px 0px 0px 0px');
    $(element).css('margin-bottom', '0%');
    $('.' + i).slideUp();
  }
}
