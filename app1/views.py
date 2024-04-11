from django.shortcuts import render ,redirect
from app1.models import Registration
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def Homepage(request):
    return render(request,'Homepage.html')
def TeacherLogin(request):
    return render(request,'TeacherLogin.html')
def StudentLogin(request):
    return render(request,'Studentlogin.html')
def Register(request):
    if request.method =="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user object with the extracted data
        new_user = Registration(name=name, number=number, email=email, password=password)
        new_user.save()
        print("The data has been written to db")


    return render(request,'Rform.html')
def student_dashboard(request):
    return render(request,'Dashboard.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page (change 'home' to the appropriate URL name)
            return redirect('dashoard/')
        else:
            # Invalid login
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'Rform.html')
def notes(request):
    return render(request,'Notes.html')
