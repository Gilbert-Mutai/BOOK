from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm,BookingForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    
    context = {"form":form}

    return render(response, "registration/register.html", context)

# Update profile

@login_required(login_url='/accounts/login/')
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
@login_required(login_url='/accounts/login/')
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


@login_required
def booking(request):
        current_user = request.user
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                applicant = form.save(commit=False)
                applicant.user = current_user
                applicant.save()
                messages.success(request, f'Your account has been successfully updated')
                return redirect('home')
        else:
            form = BookingForm()


        context = {
             'form':form

    }
        return render(request, 'book.html',context)