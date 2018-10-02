

var url_getUsers = "localhost:8000/api/user" //GET
var url_getUser = "localhost:8000/api/user/{{}}" //UPDATE
var url_updateUser = "locahost:8000/api/user/{{}}" //PUT
var url_createUser = "localhost:8000/api/user" //POST
var url_deleteUser = "localhost:8000/api/user/{{}}" //DELETE

function test() {
  alert("Message");
  // populateUserCards();
}

function populateUserCards() {
  // function get(url_getUsers) {
    jQuery.ajax({
      url: url_getUsers,
      cache: false,
      contentType: 'application/json',
      processData: false,
      type: 'GET',
      success: function(jsonres) {
        console.log(jsonres)
      },
      error: function(xhr) {
        var x = JSON.parse(xhr.responseText);
        console.log(x)
        // $('#error').text("Error ocurred at Server side: " + x.Message);
      }
    });
}

// alert("message");
