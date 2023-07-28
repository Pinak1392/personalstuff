var pagetop, yPos;
function yScroll(){
  yPos = window.pageYOffset;

  if(yPos >= 0){
    $('#pagetop').css('display', 'block');
    $('#pagetop').css('height', '20%');
    $('#pagetop').css('paddingTop', '3%');
  }

  if(yPos > 40){
    $('#pagetop').css('display', 'block');
    $('#pagetop').css('height', '5%');
    $('#pagetop').css('paddingTop', '1%');
  }

  if(yPos > 80){
    $('#pagetop').css('display', 'none');
    $('#pagetop').css('height', '0%');
    $('#pagetop').css('paddingTop', '0%');
  }
}
window.addEventListener('scroll', yScroll);

$('.nav-item').mouseover(function() {
  $(this).css('background', 'rgb(80,80,80)');
});

$('.nav-item').mouseout(function() {
  $(this).css('background', 'rgba(0,0,0,0)');
});
