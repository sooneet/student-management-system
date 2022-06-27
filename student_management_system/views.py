from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout

def base(request):
    return render(request,'base.html')

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'))
    
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse('HOD')
            elif user_type == '2':
                return HttpResponse('STAFF')
            elif user_type == '3':
                return HttpResponse('STUDENT')   
            else:
                return redirect('doLogin')                                 
    return render(request,'login.html')    