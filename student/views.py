from django.shortcuts import render,redirect,get_object_or_404
from student.models import student
from .forms import *
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
import csv
import os
# Create your views here.
def create_superuser_view(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "adminpass")
        return HttpResponse("Superuser created.")
    return HttpResponse("Superuser already exists.")

def home(request):
    print(os.getenv('CLOUDINARY_CLOUD_NAME'))
    print(os.getenv('CLOUDINARY_API_KEY'))
    print(os.getenv('CLOUDINARY_API_SECRET'))
    return render(request,"home.html")

def search(request):
    print(request.user)
    mymem=student.objects.all().values()
    context={
        'Stud_Form':StudentForm2(),
        'mymem':mymem
    }
    if request.method == 'POST':
        try:
            name=request.POST.get('name')
            if name:
                print(request.POST)
                nam = student.objects.get(name=name)
                return redirect('detail', stud_id=nam.id)
        except:
            return redirect('not_Reg')
    return render(request,'search.html',context)

def detail(request,stud_id):
    nam = student.objects.get(id=stud_id)
    return render(request,'detail.html',{'student':nam})

def not_Reg(request):
    return render(request,'not_Reg.html')

def reg_stud(request):
    context={
        'Stud_Form':StudentForm()
    }

    if request.method == 'POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'reg_stud.html',context)

def result(request):
    mymem=student.objects.all()
    p_stud=[]
    f_stud=[]
    for i in mymem:
        if i.mark > 40:
            p_stud.append(i.name)
        else:
            f_stud.append(i.name)
    con={
        'pass':p_stud,
        'fail':f_stud
    }
    return render(request,'result.html',con)

def department(request):
    mymem=student.objects.all()
    Bsc=[]
    BCom=[]
    Bba=[]
    for i in mymem:
        if i.deaprtment == 'Bsc':
            Bsc.append(i.name)
        elif i.deaprtment == 'B.Com':
            BCom.append(i.name)
        else:
            Bba.append(i.name)
    con={
        'bsc':Bsc,
        'bcom':BCom,
        'bba':Bba
    }
    return render(request,'department.html',con)


def download_csv(request):
    # Create the HttpResponse object with CSV content
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_by_department.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Fetch all students and group by department
    students = student.objects.all().order_by('deaprtment')

    # Track the current department
    current_department = None

    for s in students:
        # If the department changes, insert a department header
        if s.deaprtment != current_department:
            writer.writerow([])  # Add an empty row for separation
            writer.writerow([f"Department: {s.deaprtment}"])  # Department header
            writer.writerow(['ID', 'Name', 'Department', 'Grade', 'Mark'])  # Column headers
            current_department = s.deaprtment  # Update current department
        
        # Write student data
        writer.writerow([s.id, s.name, s.deaprtment, s.grade, s.mark])

    return response

def edit_stud(request):
    mymem=student.objects.all()
    con={
        'mymem':mymem,
    }
    return render(request,'edit.html',con)

def edit(request,stud_id):
    student_instance = get_object_or_404(student, id=stud_id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student_instance)  # Pre-fill form with data
        if form.is_valid():
            form.save()  # Save the updated data
            return redirect('edit_stud')  # Redirect to student list or another page
    else:
        form = StudentForm(instance=student_instance)  # Show form with existing data

    return render(request, 'edit_stud.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')  # Redirect to home page
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def log_in(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')

def contact(request):
    return render(request,'contact.html')