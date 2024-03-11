from .models import CustomUser

def User_context(request):
    if request.user.is_authenticated:
        if CustomUser.objects.filter(username=request.user.username).exists():
            user=CustomUser.objects.get(username=request.user.username)
        else:
            user=request.user
    else:
        user=None
    return {'User': user}