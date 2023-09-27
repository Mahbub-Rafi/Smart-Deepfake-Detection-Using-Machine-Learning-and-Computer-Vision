from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
class LoginDetialView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            action = request.POST.get('action')

            if action == 'login':
                username_ = request.POST['username']
                password_ = request.POST['password']

                myuser = authenticate(username = username_, password = password_)

                if myuser is not None: 
                    return render(request, 'home.html', {})
                else:
                    return render(request, self.template_name, {})
            elif action == 'signup':
                return redirect('signup')
            

class SignUpDetailView(View):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            action = request.POST.get('action')

            if action == 'signup' :

                username_ = request.POST['username']
                email_ = request.POST['email']
                pass1_ = request.POST['pass1']
                pass2_ = request.POST['pass2']

                if pass1_ == pass2_:
                    myuser = User.objects.create_user(username = username_, password = pass1_, email = email_)
                    myuser.save()
                    return redirect('login')
                
            elif action == 'login' :
                return redirect("login")


    
