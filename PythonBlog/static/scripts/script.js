function load(tag, title){
  console.log('/rawblog/' + tag + '/');
  $('#title').text('py.ongyang: ' + title);
  $('#page').load('/rawblog/' + tag + '/', function(){
    $('#pagewrapper').fadeIn();
  });
}

function dismiss(){
  $('#pagewrapper').fadeOut();
  $('#title').text('py.ongyang\'s blog');
}
