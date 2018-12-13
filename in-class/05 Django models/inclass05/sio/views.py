from django.shortcuts import render
from sio.models import *

# Create your views here.
def home(request):
    return render(request, 'sio.html', {})


def add_student(request):
    errors = []  # A list to record messages for any errors we encounter.
    andrewid = firstname = lastname = None

    if not 'andrew-id' in request.POST or not request.POST['andrew-id']:
        errors.append('No Andrew ID')
    else:
        andrewid = request.POST['andrew-id']

    if not 'first-name' in request.POST or not request.POST['first-name']:
        errors.append('No first name')
    else:
        firstname = request.POST['first-name']

    if not 'last-name' in request.POST or not request.POST['last-name']:
        errors.append('No last name')
    else:
        lastname = request.POST['last-name']

    new_student = Student(andrewid=andrewid, firstname=firstname, 
        lastname=lastname)
    new_student.save()

    # Sets up data needed to generate the view, and generates the view
    students = Student.objects.all()
    context = {'students':students, 'errors':errors}
    return render(request, 'sio.html', context)


def add_course(request):
    errors = []  # A list to record messages for any errors we encounter.
    courseno = coursename = instructor = None

    if not 'course-number' in request.POST or not request.POST['course-number']:
        errors.append('No course number')
    else:
        courseno = request.POST['course-number']

    if not 'course-name' in request.POST or not request.POST['course-name']:
        errors.append('No course name')
    else:
        coursename = request.POST['course-name']

    if not 'instructor' in request.POST or not request.POST['instructor']:
        errors.append('No course instructor')
    else:
        instructor = request.POST['instructor']

    new_course = Course(courseno=courseno, coursename=coursename,
        instructor=instructor)
    new_course.save()

    # Sets up data needed to generate the view, and generates the view
    courses = Course.objects.all()
    context = {'courses':courses, 'errors':errors}
    return render(request, 'sio.html', context)


def register(request):
    errors = []  # A list to record messages for any errors we encounter.
    andrewid = courseno = None
    student = course = None

    if not 'andrew-id' in request.POST or not request.POST['andrew-id']:
        errors.append('No Andrew ID')
    else:
        andrewid = request.POST['andrew-id']

    if not 'course-number' in request.POST or not request.POST['course-number']:
        errors.append('No course number')
    else:
        courseno = request.POST['course-number']

    try:
        student = Student.object.get(andrewid=andrewid)
    except ObjectDoesNotExist:
        errors.append('Student not found')

    try:
        course = Course.object.get(courseno=courseno)
    except ObjectDoesNotExist:
        errors.append('Course not found')

    new_registration = Registration(student=student, course=course)
    new_registration.save()

    # Sets up data needed to generate the view, and generates the view
    registrations = Registration.objects.all()
    context = {'registrations':registrations, 'errors':errors}
    return render(request, 'sio.html', context)

