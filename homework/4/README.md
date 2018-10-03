# Homework 4

### Applications

​	For modularity purpose, I devided the whole project into 3 separate applications, each of which takes 				responsibility of certain part of work:

###### 1. authentication

​	Handles signup, login, email verification and reseting password.

​	Models: None

​	Forms: SignupForm

###### 2. grumblr

​	The main application, responsible for functions related to Global Stream, User Profile, and Follower Stream pages.

​	Models: Post

​	Forms: PostForm

###### 3. profiles

​	Responsible for Profile model. Deals with editing profile, getting profile images, following and unfollowing.

​	Models: Profile

​	Forms: ProfileForm

### Models

###### 1. Post

​	The users' posts. It has User as its foreignkey, with other fields including text, time and image. image field can be none. If user create a Post without uploading image, only the text would appear in the stream.

###### 2. Profile

​	The users' profile. It extends Django's User model. It has User as its OneToOneField. Instead of using User's first_name and last_name in this project, I defined first_name and last_name field in Profile so that it would be easier to edit them later. Other fields include age, which is an integer between 0 to 100, bio, which is less than 420 characters, and image. These 3 fields can be none, and user can edit them any time. It also has a ManyToManyField to store the follow and unfollow relationships.

### Forms and ModelForms

###### 1. SignupForm

​	To submit data when registering a new account.

###### 2. PostForm

​	The ModelForm of Post. It submits data when user creates a new post. A new Post instance will then be created.

###### 3. ProfileForm

​	The ModelForm of Profile. It submits data when user edits his/her profile. The Profile instance of this user will then be updated.

### Template Inheritance

###### 1. base.html

​	It defines some common webpage appearance. Global Stream, Edit Profile, User Profile and Follower Stream extend it.

###### 2. login.html

​	It originally responsed for the login page appearance. Then some pages related to password resetting extend it.

### New Features Implementation

###### 1. Image upload

​	Images uploaded with Post are stored in media/post_images. It can be retrieved by the post id.

​	Images uploaded when editing profile are stored in media/profile_images. It can be retrieved by the username corresponding to the Profile.

###### 2. Edit profile

​	Created a new page for editing profile. It works by submitting a ProfileForm.

###### 3. Follow and Unfollow

​	When user A follows user B, a ManyToMany relationship between A's Profile and B's User is created in A's Profile.followers. When A unfollows B, this relationship is removed.

​	All the Posts of users that A follows will appear in A's Follower Stream page, as well as a list of usernames of them that can link to their profile pages.

###### 4. Email Verification

​	When clicking 'signup' in signup page, an email will appear in the terminal. Users can copy the link in the email into browser, and will be redirected to login page immediately if the verification succeeds, or be redirected to signup page if the verfication fails.

###### 5. Reset Password

​	Used the Views defined in django.contrib.auth.views to implemented the password resetting. When clicking 'Reset Password' link on the login page, users will be redirected to a page to submit their email address. Then an email will appear in the terminal. Users can copy the link in the email into browser, and will enter a page to submit new password. Then they will be redirected to a page showing that the resetting is successful. Then they can go to the login page again and login with the new password.

​	