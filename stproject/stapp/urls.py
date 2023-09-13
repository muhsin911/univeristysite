from django.urls import path
from .import views

app_name = 'stapp'

urlpatterns = [
    path('',views.allCourseDept,name='allcat'),
    path('studentreg/',views.studentreg,name='form'),
    path('coursedetails/',views.coursedet,name='rcourse'),
    path('get_courses_by_department/<int:department_id>/', views.get_courses_by_department, name='get_courses_by_department'),
    path('touch/',views.getintouch,name='rtouch'),
    ]