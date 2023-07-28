//Current slide
var curSlide = 1;

var correct = 0;
var qCorrect = [0, 0, 0, 0, 0]

function hint(){
  $('.hint' + String(curSlide)).fadeIn();
}

function questionResult(answer){
  var answer = answer.inputbox.value;
  if(answer === answerList[curSlide - 1]){
    $(".r" + String(curSlide)).fadeIn("slow");
    qCorrect[curSlide - 1] = 1
    console.log(qCorrect);
    correct++;
  } else {
    $(".w" + String(curSlide)).fadeIn("slow");
  }

  $('.s' + String(curSlide)).css('display', 'none');
  $('.n' + String(curSlide)).fadeIn();
}

function nextSlide (){
  $('#qSlider .slides').animate({'margin-left':'-=100%'}, 1000);
  curSlide++;
  if (curSlide == answerList.length + 1){
    $('.boxes').css('display', 'block')
    $('.clickResult').css('display', 'block')
  }
}

function results (){
  function resultShow(i){
      if(qCorrect[i -1] === 1){
        $('.b' + String(i)).css('background', 'limeGreen');
      } else {
        $('.b' + String(i)).css('background', 'red');
      }
  }

  var percent = String((correct*100)/answerList.length) + '%';
  var percent2 = String(((correct*100)/answerList.length) + 5) + '%';
  alert(percent + ' correct.')
  $('.clickResult').css('display', 'none');
  for(var i = 0; i < qCorrect.length + 1; i++){
    resultShow(i);
  }
}
