### Homework 5

python version: 3.7.0

##### 1. Update:

​	When the html page is ready, in js files, call initialPostlist() function to display all existing posts and their comments.

​	Set a "max-time" key in posts.json to keep track of the most recent time when a post was added. Call getUpdates() function in javascript files every 5 seconds. In every update, retrieve only the posts that were created later than the max-time, and add them into the list in the himl page, without refreshing the whole page. Also update the max-time in getUpdates() to make sure its the max time of all the posts so far.

​	When adding a new post, addPost() function in js file react to the click of Add Post button, and calls add_post() function in views.py. Then, call getUpdates() function in js file immediately to display the post list with the newly added post.

##### 2. Comments:

​	Create a new model called "Comment", which has the fields of post, user, text, time. When first loading the web page, get every existing post, and call displayComments() in js, which calls getComments(post_id) for every post to get their comments.

​	When adding a new comment for, simply call getComments(post_id) for that post to update the comments of this post. The newly added comments won't be displayed in another user's page in getUpdates() unless refreshing the page, as it is not required for this homework.