from django.urls import path
import sio.views

urlpatterns = [
    path('', sio.views.home),
    path('create-student', sio.views.add_student),
    path('create-course', sio.views.add_course),
    path('register', sio.views.register),
]
