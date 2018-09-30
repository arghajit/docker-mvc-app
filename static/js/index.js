
function init() {
  console.log('init');
  var cards = document.querySelectorAll('.card:not(.inactive)');
  for(var i = 0 ; i<cards.length ; i++) {
    console.log(cards[i]);
    cards[i].addEventListener('click',function(){
      console.log('clicked');
      document.querySelector('.card-stack').style.display='none';
      document.querySelector('.details-stack').style.display='block';
    });
  }
  goback();
}
function reset() {
  location.reload();
}
function myfuc(obj) {
  console.log('clicked');
  document.querySelector('.card-stack').style.display='none';
  document.querySelector('.details-stack').style.display='block';

  // alert(obj.text)
  // console.print("hello");
    // alert ("Hello World!");
}

function goback() {
  document.querySelector('.card-stack').style.display='block';
  document.querySelector('.details-stack').style.display='none';
}

function post(data, url) {

  $('#loader').css("display", "inline-block");
  jQuery.ajax({
      url: url,
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      type: 'POST',
      success: postSuccess,
      error: function(xhr) {
        var x = JSON.parse(xhr.responseText);
        $('#error').text("Error ocurred at Server side: " + x.Message);
      }
    });
  }

function get(url) {
  jQuery.ajax({
    url: url,
    data: data,
    cache: false,
    contentType: false,
    processData: false,
    type: 'GET',
    success: getSuccess,
    error: function(xhr) {
      var x = JSON.parse(xhr.responseText);
      $('#error').text("Error ocurred at Server side: " + x.Message);
    }
  });
}

function getSuccess(jsonresponse) {

}

function addCard(name) {
  var div = document.createElement('div');
  div.className = 'card';
  div.innerHTML =
      '<a href="">'+name+'</a>';
  document.getElementById('stack').appendChild(div);
}

function removeRow(input) {
  var cards = document.getElementById('stack').getElementsByClassName('card');
  for(var i = 0;i<cards.length;i++) {
    if(cards[i].textContent=input) {
    document.getElementById('stack').removeChild(cards[i]);
    }
  }
}