// The boilerplate code below is copied from the Django 1.10 documentation.
// It establishes the necessary HTTP header fields and cookies to use
// Django CSRF protection with jQuery Ajax requests.

$( document ).ready(function() {  // Runs when the document is ready

  // using jQuery
  // https://docs.djangoproject.com/en/1.10/ref/csrf/
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  // TODO:  Use jQuery to send an Ajax GET request to /sio/get-courses and
  // update the list of courses on the web page.  (Use our provided
  // helper method, updateChanges, below.)



  $('#create-student-form').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted

      // TODO:  Use jQuery to send an Ajax POST request to /sio/create-student.
  });


  $('#create-course-form').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted

      // TODO:  Use jQuery to send an Ajax POST request to /sio/create-course.
  });


  $('#register-student-form').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted

      // TODO:  Use jQuery to send an Ajax POST request to /sio/register-student.
  });


  // The following function will help you update the contents of the
  // page based on our application's JSON response.
  function updateChanges(data) {
    // Clear old messages
    $('#messages').empty();

    // Display new messages
    for(var i = 0; i < data.messages.length; i++) {
      $('#messages').append('<li>' + data.messages[i] + '</li>');
    }

    // Process courses
    for(var i = 0; i < data.courses.length; i++) {

      // Add course by course number
      var course_num = data.courses[i]['course_number'];
      if($('#course-' + course_num).length == 0) {
        $('#courses-list').append('<li>' + data.courses[i]['course'] + '<ul id="course-' + course_num + '"></ul></li>');
      } else {
        $('#course-' + course_num).empty() // Clear students from existing course
      }

      // Add students to course
      for(var j = 0; j < data.courses[i]['students'].length; j++) {
        $('#course-' + course_num).append('<li>' + data.courses[i]['students'][j] + '</li>');
      }
    }

    // Update timestamp
    $('#timestamp').val(data.timestamp);
  }

}); // End of $(document).ready
