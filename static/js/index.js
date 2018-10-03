
var userArray;

function updateArray(JSONString) {
  console.log("Updating array")
  userArray = JSON.parse(JSONString);
  console.log(userArray);
}

function getFromArray(id) {
  return userArray[id];
}

function getCountFromArray() {
  return userArray.length;
}

function refreshUserDataSet() {
  console.log("GET all users")
  jQuery.ajax({
    url: url_getUsers,
    // cache: false,
    // contentType: 'application/json',
    // processData: false,
    type: 'GET',
    success: function(successjson) {

      console.log(successjson)
      updateArray(successjson);
      populateCount();
    },
    error: function(xhr) {
      var x = JSON.parse(xhr.responseText);
      console.log(x)
      document.getElementById('error').style.display='block';
    }
  });
}

function populateCardsInStack() {
  console.log("starting populating the card stack");
  var cardstack = document.getElementById('stack');
  for (i = 0; i < getCountFromArray; i++) {

    var user = getFromArray(i);

    var div = document.createElement('div');
    var a = document.createElement('a');
    var text = document.createTextNode(user['name']);

    div.className = 'card';
    // a.href = slugify(user['name']);

    a.appendChild(text);
    div.appendChild(a);
    cardstack.appendChild(div);
  }
  console.log("populated")
}

function populateCount() {
  console.log("populating count fields")
  document.getElementById('count').textContent=getCountFromArray();
}

function generateCreateUserView() {
  toggleDetail();
  // document.getElementById('')
  // generate with ext. dom and css
  // use this as onclick on add button
}

function performCreate(name,birthday,email,address) {
  //perform a form action POST
  //on  success
  refreshUserDataSet();
  populateCardsInStack();
  populateCount();
  toggleDetail();
}

function performUpdate(name) {
  // form data
  // on success
  //on  success
  refreshUserDataSet();
  populateCardsInStack();
  populateCount();
  toggleDetail();
}

function performDelete(name) {
  jQuery.ajax({
    url: url_deleteUser.replace("{{}}",slugify(name)),
    // cache: false,
    // contentType: 'application/json',
    // processData: false,
    type: 'DELETE',
    success: refreshUserDataSet,
    error: function(xhr) {
      var x = JSON.parse(xhr.responseText);
      console.log(x)
      toggleDetail();
      document.getElementById('error').style.display='block';
      // document.getElementById('error').style.display='block';
      // $('#error').text("Error ocurred at Server side: " + x.Message);
    }
  });

}

function slugify(text) {
  return text.replace(/ /g,"_");
}

function toggleDetail() {
  console.log("toggle view")
  document.querySelector('.card-stack').style.display='block';
  document.querySelector('.details-stack').style.display='none';
}

//data: JSON.stringify({ name : "AA" }),

function start() {
  console.log('start');
  alert('start');
  refreshUserDataSet();
  // updateArray()
  populateCardsInStack();
}

var url_getUsers = "http://127.0.0.1:8000/api/user" //GET
var url_getUser = "http://127.0.0.1:8000/api/user/{{}}" //UPDATE
var url_updateUser = "http://127.0.0.1:8000/api/user/{{}}" //PUT
var url_createUser = "http://127.0.0.1:8000/api/user" //POST
var url_deleteUser = "http://127.0.0.1:8000/api/user/{{}}" //DELETE

// var html_a_card = "<div class="card"><a href="{{}}">{{}}</a></div>"
//
//
// function populateUserCards() {
//   jQuery.ajax({
//     url: url_getUsers,
//     // cache: false,
//     // contentType: 'application/json',
//     // processData: false,
//     type: 'GET',
//     success: getSuccess,
//     error: function(xhr) {
//       var x = JSON.parse(xhr.responseText);
//       console.log(x)
//       $('#error').text("Error ocurred at Server side: " + x.Message);
//     }
//   });
//
//   document.getElementById('tag-id').innerHTML = '<ol><li>html data</li></ol>';
// }
//
// function initPage() {
//   console.log('init');
//   populateUserCards();
//   var cards = document.querySelectorAll('.card:not(.inactive)');
//   for(var i = 0 ; i<cards.length ; i++) {
//     console.log(cards[i]);
//     cards[i].addEventListener('click',function(){
//       console.log('clicked');
//       document.querySelector('.card-stack').style.display='none';
//       document.querySelector('.details-stack').style.display='block';
//     });
//   }
//   // goback();
// }
// function reset() {
//   location.reload();
// }
// function myfuc(obj) {
//   console.log('clicked');
//   document.querySelector('.card-stack').style.display='none';
//   document.querySelector('.details-stack').style.display='block';
//
//   // alert(obj.text)
//   // console.print("hello");
//     // alert ("Hello World!");
// }
//
// function goback() {
//   document.querySelector('.card-stack').style.display='block';
//   document.querySelector('.details-stack').style.display='none';
// }
//
//
//
// function post(data, url) {
//
//   $('#loader').css("display", "inline-block");
//   jQuery.ajax({
//       url: url,
//       data: data,
//       cache: false,
//       contentType: false,
//       processData: false,
//       type: 'POST',
//       success: postSuccess,
//       error: function(xhr) {
//         var x = JSON.parse(xhr.responseText);
//         $('#error').text("Error ocurred at Server side: " + x.Message);
//       }
//     });
//   }
//
// function get(url) {
//   jQuery.ajax({
//     url: url,
//     data: data,
//     cache: false,
//     contentType: false,
//     processData: false,
//     type: 'GET',
//     success: getSuccess,
//     error: function(xhr) {
//       var x = JSON.parse(xhr.responseText);
//       $('#error').text("Error ocurred at Server side: " + x.Message);
//     }
//   });
// }
//
// function getSuccess(jsonresponse) {
//   console.log(jsonresponse)
//
// }
//
// function addCard(name) {
//   var div = document.createElement('div');
//   div.className = 'card';
//   div.innerHTML =
//       '<a href="">'+name+'</a>';
//   document.getElementById('stack').appendChild(div);
// }
//
// function removeRow(input) {
//   var cards = document.getElementById('stack').getElementsByClassName('card');
//   for(var i = 0;i<cards.length;i++) {
//     if(cards[i].textContent=input) {
//     document.getElementById('stack').removeChild(cards[i]);
//     }
//   }
// }
//
// function slug(text) {
//   return text.repla
// }
// }
