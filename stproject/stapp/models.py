from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    objects = None
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='Product', blank=True)

    class Meta:
        ordering=('name', )
        verbose_name='Department'
        verbose_name_plural='Departments'

    def get_url(self):
        return reverse('stap:allcat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):

    objects = None
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    fees=models.DecimalField(max_digits=10,decimal_places=2)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Product',blank=True)
    no_of_seats=models.IntegerField()
    # purpose=models.TextField(blank=True)

    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    # def get_url(self):
    #     return reverse('stapp:course_by_dept',args=[self.department.slug,self.slug])

    class Meta:
        ordering=('name', )
        verbose_name='Course'
        verbose_name_plural='Courses'



    def __str__(self):
        return '{}'.format(self.name)
