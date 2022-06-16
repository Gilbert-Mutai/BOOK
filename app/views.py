from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .email import send_welcome_email,send_admin_email,send_booking_email
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm,BookingForm
from .utils import station_time

# Create your views here.
def index(request):
    page='Home'
    context={
        'page':page,
    }
    return render(request,'index.html',context)


def about_us(request):
    page='About us'
    context={
        'page':page,
    }
    return render(request,'about.html',context)


def contact_us(request):
    page = 'Contact us'
    context={
        'page':page,
    }
    return render(request,'contact.html',context)


def stations(request):
    page = 'Stations'
    context={
        'page':page,
    }
    return render(request,'stations.html',context)


def register(response):
    page = 'Account'
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']

            request = form.save(commit=False)
            name = request.username
            email = request.email

            admin_name='Captain'

            send_welcome_email(name,email)
            send_admin_email(admin_name,name)

            request.save()
            return redirect("login")
    else:
        form = RegisterForm()
    
    context = {
        "form":form,
        "page":page,
    
    }

    return render(response, "registration/register.html", context)

# Update profile

@login_required(login_url='/login/')
def updateprofile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    }

    return render(request, 'profile/edit_profile.html', context)

# Profile
@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    }
    return render(request, 'profile/profile.html', context)

@login_required(login_url='/login/')
def booking(request):
        current_user = request.user
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                From = form.cleaned_data['From']
                date = form.cleaned_data['date']
                applicant = form.save(commit=False)

                applicant.user = current_user

                From=applicant.From

                date = applicant.date

                time =station_time[From]
            
                name = request.user
                email = request.user.email


                send_booking_email(name,email,From,date,time)

                applicant.save()
                messages.success(request, f'Your account has been successfully updated')
                return redirect('home')
        else:
            form = BookingForm()


        context = {
             'form':form

    }
        return render(request, 'book.html',context)