$.ajax({
  type: "POST",
  contentType: 'application/json',
  url: "/login",
  data: {},
  dataType: "json",
  success: function(result) {
    console.log("it works!!");
    document.write(response);
  } 
});