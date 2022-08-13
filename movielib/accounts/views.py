from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def index(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('accounts:index')
            elif User.objects.filter(email=email).exists() :
               messages.info(request,"Email taken")
               return redirect('accounts:index')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email = email,
                    password=password
                )
                user.save()
                print("user created")
        else :
            messages.info(request,"password do not match")
            return redirect('accounts:index')
        
        
        return redirect("accounts:login")
     
    else:
        return render(request, 'accounts/index.html')

def login(request) :
    if request.method == 'POST' :
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)

       if user is not None:
            auth.login(request,user)
            print('success')
            return redirect("movies:index")
       else:
        messages.info(request,'invalid credentials')
        return redirect('accounts:login')
    else :
        return render(request, 'accounts/login.html')

    
def logout(request):
    auth.logout(request)
    return redirect('/')

