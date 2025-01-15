from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import  Train_data, Station, ClassTypes
from datetime import datetime
from django.db.models import Q
from . models import Station,Passenger
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('signup')

        # Create user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, 'Your account has been successfully created')
        return redirect('signin')
    
    return render(request, "signup.html")

# Signin view
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        # Authenticate user
        user = authenticate(username=username, password=pass1)

        if user is not None:
            # Login user
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('signin')

    return render(request, "signin.html")

# Signout view
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')

def index(request):
    station=Station.objects.all()
    return render(request, 'index.html',{'station':station})

def search_results(request):
    if request.method == "POST":
        source = request.POST['source']
        destination = request.POST['destination']
        date = request.POST['date']
        station = Train_data.objects.filter(source=source,destination=destination, departure_date=date)
        return render(request, 'search.html',{'st':station})
    return render(request, 'search.html')

def trainlist(request):
    trains = Train_data.objects.all()

    return render(request,'Trains.html', {'trains':trains})
def book_ticket(request):
   if request.method == 'POST':
        # Capture and save passenger details
        p_name = request.POST.get('passengername')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        seat_preference = request.POST.get('seatpreference')
        departure= request.POST.get('departure')
        destination = request.POST.get('destination')

        # Save the passenger details to the Passenger model
        Passenger.objects.create(
            passenger_name=p_name,
            age=age,
            gender=gender,
            seat_preference=seat_preference,
            departure=departure,
            destination=destination
        )

        # Redirect to confirmation page or show success message
        messages.success(request, 'Booking and passenger details saved successfully!')
        return redirect('booking',p_name= p_name)
   

def booked(request,p_name):
        book= Passenger.objects.filter(passenger_name=p_name).order_by('-id').first()
        
        return render(request, 'booking.html',{'book':book})
    