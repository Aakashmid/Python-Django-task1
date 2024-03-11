from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return render(request,'app/login.html')
    else:
        return render(request,'app/index.html')
def signuphand(request):
    pass
def loginhand(request):
    pass
def logouthand(request):
    pass