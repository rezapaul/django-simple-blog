from django.shortcuts import render ,redirect ,get_list_or_404
from django.contrib.auth.models import User
from django.contrib import messages , auth
from .models import Profile



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        bio = request.POST['bio']
        photo = request.FILES.get('photo')
        if password == password2:
            if User.objects.all().filter(username=username).exists():
                messages.error(request,'This username already exists')
                return redirect('register')
            else: 
                if User.objects.all().filter(email=email).exists():
                    messages.error(request,'This email is used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name , last_name=last_name , username=username , email=email , password=password) 
                    user.save()
                    profile = Profile(user=user, bio=bio, photo=request.FILES.get('photo'))
                    profile.save() 
                    messages.success(request,'You registered successfully ,you can login now')
                    return redirect('login')  
        else :
            messages.error(request,'Password do not match')  
            return redirect('register')  
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You logged out successfully')
        return redirect('index')        
