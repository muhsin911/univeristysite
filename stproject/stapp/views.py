from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from stapp.models import Department,Course




def allCourseDept(request):
    depts = Department.objects.all()
    courses =Course.objects.all()
    return render(request, 'index.html', {'depts':depts, 'courses':courses})


from django.shortcuts import render
from .models import Department, Course

def studentreg(request):
    departments = Department.objects.distinct().order_by('name')
    return render(request, 'form.html', {'departments': departments})


def get_courses_by_department(request, department_id):
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def coursedet(request):
    depts = Department.objects.all()
    courses =Course.objects.all()
    return render(request, 'course.html', {'depts':depts, 'courses':courses})


def getintouch(request):
    return render(request, 'getintouch.html')







