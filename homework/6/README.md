

# Homework 6

## 1. Deployment and Configurations

1. Deployed on AWS (Amazon Web Services) by creating an EC2 instance as an Ubuntu machine.

   I can connect to the machine with "ssh -i "LyuliangLiu.pem" ubuntu@ec2-3-16-163-92.us-east-2.compute.amazonaws.com"

2. Installed Apache web server, and used mod_wsgi plugin.

3. One configuration file: 000-default.conf is commited with the project.

4. The website can be visited with the IP address: http://3.16.163.92/ 

   (or http://ec2-3-16-163-92.us-east-2.compute.amazonaws.com)



## 2. Email configurations

Set the environment variables of id and password of my email in the Apache configuration file. Then in settings.py of my django project, use 

```
EMAIL_HOST_USER = os.environ['id']
EMAIL_HOST_PASSWORD = os.environ['password']
```

to configure the email address and password to send the verification emails when registering new users and resetting password.

The email host I used is 'smtp.andrew.cmu.edu', and the DEFAULT_FROM_EMAIL is 'Grumblr <<lyulianl@andrew.cmu.edu>>'

## 3. Serving static contents

Since I have seperated the whole project into three applications, I used ./manage.py collectstatic to collect all static files into a folder '/static/' under the root directory. 

In settings.py, set 

```
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```

This way, all static content will be retrieved from this directory.



###### Citings:

https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html
