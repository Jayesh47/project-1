from django.shortcuts import render, HttpResponseRedirect
from .models import student
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method == "POST":
        student_name = request.POST['std_name']
        student_email = request.POST['std_email']
        student_password = request.POST['std_pass']
        
        result = student(student_name=student_name, student_email=student_email, student_password=student_password)
        result.save()
    fetch_data = student.objects.all()
    data = student.objects.all().values()
    context = {
        "AllData": fetch_data,
    }
    return render(request, 'index.html', context)

def delete(request, id):
    result = student.objects.get(student_id = id)
    result.delete()
    return HttpResponseRedirect(reverse("index"))

def edit(request, id):
    result = student.objects.get(student_id = id)
    context = {
        "student_id":result.student_id,
        "student_name":result.student_name,
        "student_email":result.student_email,
        "student_password":result.student_password,
    }
    return render(request, "edit.html", context)

def update(request, id):
    if request.method == "POST":
        result = student.objects.get(student_id = id)
        result.student_name = request.POST['std_name']
        result.student_email = request.POST['std_email']
        result.student_password = request.POST['std_pass']
        result.save()
    return HttpResponseRedirect(reverse("index"))