function initialPosts() {

    $.get("/grumblr/get_posts/")
      .done(function(data) {

          var list = $("#post_list");
          list.data('max-time', data['max-time']);
          list.html('')
          getUpdates();
          for (var i = 0; i < data.posts.length; i++) {
              post = data.posts[i];
              var new_post = $(post.html);
              list.append(new_post);
          }
      });
}

function addPost(){
    var post_text = $("#text")

    $.post("/grumblr/add_post/", {text: post_text.val()})
      .done(function(data) {

          getUpdates();
          post_text.val("").focus();
      });
}

function getUpdates() {
    var list = $("#post_list")
    var max_time = list.data("max-time")
    console.log("max_time in updates", max_time)
    $.get("/grumblr/get_posts/"+ max_time)
      .done(function(data) {
          list.data('max-time', data['max-time']);
          for (var i = 0; i < data.posts.length; i++) {
              var post = data.posts[i];
              var new_post = $(post.html);
              list.prepend(new_post);
          }
      });
}

$(document).ready(function () {
  // Add event-handlers
  $("#add_post").click(addPost);

  // Set up to-do list with initial DB items and DOM data
  initialPosts();

  // Periodically refresh to-do list
  window.setInterval(getUpdates, 5000);

  // CSRF set-up copied from Django docs
  function getCookie(name) {  
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
});
