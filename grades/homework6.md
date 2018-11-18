Homework 6 Feedback
==================

Commit graded: 1183f740525485538840407a276276290b94630a

### Incremental development using Git (10/10)

### Fulfilling our specification (23/50)
* -5, Passwords, access keys, and other sensitive information should never be committed in a repository accessible by multiple people. Your code reflects that you are committing the `SECRET_KEY` in settings.py
* -2, Your `ALLOWED_HOSTS` setting is too permissive. Allowing too many hostnames opens your site up to CSRF attacks.
* -2, You should not run with `DEBUG = True` in production.
* -20, The data should be stored in a relational database that is not SQLite. SQLite is a lightweight database that cannot handle production-level load. For example, SQLite does not allow for concurrent access of data, which means that performance would be very poor if multiple users used your site.

### Responding to hw5 feedback (20/20)

---
#### Total score (53/80)
---
Graded by: David Yang (dzy@andrew.cmu.edu)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/lyulianl/blob/master/grades/homework6.md

