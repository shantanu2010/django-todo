from .auth import *
from django import forms
from django.views import *
from django.shortcuts import render,redirect
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse


def logout_user(request):
    logout(request)
    return redirect("login")

class SignupForm(forms.Form):

    first_name = forms.CharField(
        max_length= 75,
        required = True,
        widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'First Name','label':'First Name'})

    )

    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'label': 'Last Name'})

    )

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'label': 'username'})

    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'label': 'password'})

    )


class renderForm(View):
    def get(self, request):
        form = SignupForm()

        return render(request,template_name="signup.html",context={'form':form})


    def post(self,request):

        form = SignupForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(

                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],

            )

            if user is not None:
                login(request,user)
                return redirect("cards")

            else:

                return HttpResponse("shit")


        else:
            return HttpResponse("shit")




class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName', 'label': 'UserName'})

    )

    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'label': 'Password'})

    )


class renderLogin(View):

    def get(self, request):
        form = LoginForm()

        return render(request,template_name="login.html",context={'form':form})

    def post(self,request):

        import ipdb
        form = LoginForm(request.POST)

        #ipdb.set_trace()
        if form.is_valid():

            user = authenticate(request,username=form.cleaned_data["username"],password=form.cleaned_data["password"])

            if user is not None:
                login(request, user)
                return redirect("cards")


            else:

                return HttpResponse("shit")

        else:

            return HttpResponse("shit")