function login(a){
  $(a[0]).css('background', 'white');
  $(a[1]).css('background', 'white');
  if(a[0].value !== '' && a[1].value !== ''){
    alert('Username or password is incorrect');
  } else {
    alert('One or more required fields are missing');
    for(var i = 0; i < a.length; i++){
      if(a[i].value === ''){
        $(a[i]).css('background', 'rgba(200,0,0,0.3)');
      }
    }
  }
}

function enter(a){
  for(var i = 0; i < a.length; i++){
      $(a[i]).css('background', 'white');
  }

  var missing = false;
  for(var i = 0; i < a.length; i++){
    if(a[i].value === ''){
      $(a[i]).css('background', 'rgba(200,0,0,0.3)');
      missing = true;
    }
  }
  if(missing){
    alert('One or more required fields are missing');
  } else {
    alert('Check your email for verification');
  }
}

function signUp(){
  $('.login').fadeOut('normal', function(){
    $('.signup').fadeIn();
  });
}

function back(){
  $('.signup').fadeOut('normal', function(){
    $('.login').fadeIn();
  });
}
