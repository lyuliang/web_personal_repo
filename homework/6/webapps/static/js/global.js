function initialPosts() {

    $.get("/grumblr/get_posts/")
      .done(function(data) {

          var list = $("#post_list");
          list.data('max-time', data['max-time']);
          list.html('')
          for (var i = 0; i < data.posts.length; i++) {
              var new_post = $(data.posts[i].html);
              list.append(new_post);
          }
          displayComments();
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

function addComment(post_id){
    var comment_text = $("#comment_text"+post_id);
    $.post("/grumblr/add_comment/" + post_id, {"comment_text": comment_text.val()})
        .done(function(data) {
        getComments(post_id);
        comment_text.val("")
    });
}

function displayComments() {
    var post_list = $("#post_list");
    var posts = post_list.children("div.jumbotron");
    for (var i = 0; i < posts.length; i++) {
        var post = posts[i];
        getComments(post.id);
    }
}

function getComments(post_id) {
    var comment_list = $("#comment_list" + post_id);
    comment_list.html("")
    $.get("/grumblr/get_comments/" + post_id)
        .done(function(data){
            for (var i = 0; i < data.comments.length; i ++) {
                comment_list.prepend(data.comments[i].html)
            }
        });
}

function getUpdates() {
    var list = $("#post_list")
    var max_time = list.data("max-time")
    $.get("/grumblr/get_posts/"+ max_time)
      .done(function(data) {
          list.data('max-time', data['max-time']);
          for (var i = 0; i < data.posts.length; i++) {
              var new_post = $(data.posts[i].html);
              list.prepend(new_post);
              getComments(data.posts[i].id);
          }
      });
}

$(document).ready(function () {
  // Add event-handlers
  $("#add_post").click(function (e) {
      e.preventDefault();
      addPost();
  });

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
