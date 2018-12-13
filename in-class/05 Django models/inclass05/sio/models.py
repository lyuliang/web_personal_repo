from django.db import models

class Student(models.Model):
	andrewid = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)

	def __str__(self):
		return self.andrewid + self.firstname + self.lastname

class Course(models.Model):
	courseno = models.IntegerField()
	coursename = models.CharField(max_length=200)
	instructor = models.CharField(max_length=200)
	students = models.ManyToManyField(Student, through='Registration')

	def __str__(self):
		return '{} {} {}'.format(self.courseno, self.coursename,
			self.instructor)

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
    	return '{} || {}'.format(student.__str__(), course.__str__())
