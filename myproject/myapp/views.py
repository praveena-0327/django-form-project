#-*- coding: utf-8 -*-

from django.shortcuts import render

from myapp.forms import LoginForm

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      # Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'loggedin.html', {"username" : username})
