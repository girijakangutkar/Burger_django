#from django.contrib import admin
from django.urls import path
from . import views
from app.views import SignUp, user_login, ThanksPage
app_name = 'app'

urlpatterns = [
  path('signup/',views.SignUp,name='signup'),
  path('login/',views.user_login,name='login'),
  path('thanks/', ThanksPage.as_view(),name='thanks'),
  
 
]