from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        User.objects.create_user(username=username,password=password)
        return redirect('login')

    return render(request,'register.html')


from django.contrib.auth import authenticate,login

def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')

        return render(request,'login.html',{'error':'invalid username or password'})
    return render(request,'login.html')


from django.contrib.auth.decorators import login_required
@login_required
def profile(request):

    
    if request.user.is_authenticated:
        print("user is logged in")
    else:
        print("user is not logged in")
    return render(request,'profile.html')



from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')




        


# Create your views here.
