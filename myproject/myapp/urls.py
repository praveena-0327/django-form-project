from django.views.generic import TemplateView
from django.urls import path
from .views import login

urlpatterns = [
    path('connection/',TemplateView.as_view(template_name = 'login.html')),
    path('login/', login, name = 'login') 
]