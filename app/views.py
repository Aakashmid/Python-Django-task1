from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return render(request,'app/login.html')
    else:
        return render(request,'app/index.html')
def signuphand(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('Email')
        password=request.POST.get('password')
        profile_img=request.FILES.get('profile_img')
        confirm_password=request.POST.get('confirm_password')
        Add1=request.POST.get('add1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        if city!=state:
            address=Add1+" "+city+" "+state+" "+pincode
        else:
            address=Add1+" "+state+" "+pincode

        if password != confirm_password:
            messages.error(request,'Confirm password is wrong !!')
            return HttpResponseRedirect(reverse('app:Create account'))
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request,'Username is already taken !!')
            return HttpResponseRedirect(reverse('app:Create account'))
        else:
            user=CustomUser.objects.create_user(username=username,password=password,email=email)
            user.first_name=firstname
            user.last_name=lastname
            user.address=address
            # if profile_img is not None:
            user.profileImg=profile_img
            user.save()
            login(request,user=user)
            messages.success(request,'Account is created successfully !1')
            return HttpResponseRedirect(reverse('app:home'))
    return render(request,'app/signup.html')
def loginhand(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        authenticated_user=authenticate(username=username,password=password)
        if authenticated_user:
            login(request,authenticated_user)
            messages.success(request,'Successfully logged in !!')
            return HttpResponseRedirect(reverse('app:home'))
        else:
            messages.error(request,'Username or password is wrong !!')
            return HttpResponseRedirect(reverse('app:home'))

    return render(request,'app/login.html')
def logouthand(request):
    logout(request)
    messages.success(request,"Successsfully logout !!")
    return redirect('/')