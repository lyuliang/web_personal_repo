These are the source codes for a nano-belogging site, ​grumblr​.

The features of this site include the following:

1. Non-logged-in, non-registered users may register for the site. New users must provide a username, 	first name, last name, and password. Registering for the site leaves the user logged in as the newly-registered user.

2. Registered users may log in using their username and password.

3. Logged-in users are able to post a short (42 characters or less) message. Posts, when displayed, show the following information: the contents of the post, the user who posted it (linking to the user’s profile), and the date and time the post was written.

4. Logged-in users may view a 'global stream', displaying all posts that have beeposted in reverse-chronological order (most recent first).

5.  Logged-in users may view profiles of other users (or their own profiles) when clicking on links provided with posted messages in the     global stream. Profile pages contain information about a user (e.g. first name and last name) as well as all of the posts that user has made, in reverse-chronological order.

6.  Logged-in users are able to log out.


Some behavior of the pages:

1. When visit localhost:8000, user will be redirected to localhost:8000/login/, which is associated to function log() in views.py. 
2.  log() would check if the username and password are valid, and if any required field is empty. After authentication, it will log in and redirect to /global/, which is associated to function() home. 
3. signup() would check if the new username already exists, and if any required field is empty. On creating a new user successfully, it will directly enter the global stream page for the new user, skipping the login page.
4. home() would add a Post() object into the database when user create a new post which is less than 42 character. If it is more that 42, it would show a reminding message to the user.
5. On clicking the username of each post on the global stream, user will enter the /profile/username, the profile page of that user, the behavior of which is defined in function profile(). Currently, a user's profile contains her username, firstname and lastname. On clicking View My Profile, user will enter her own profile page. On clicking Back to Stream, user will enter the global stream page again. 
6. Any behavior like refreshing or returning back to last page will not cause error. If user tries to access global page or some user's profilepage, she will first be redirected to the login page. After login, she will enter the page she intended to access.
7. This site currently does not support image content in the posts.