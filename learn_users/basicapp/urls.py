from django.urls import path
from basicapp import views

 # template urls
app_name='basicapp'

urlpatterns=[
    path('register/',views.register,name = 'register'),
    path('login/',views.user_login,name = 'login'),
    path('profile/',views.profile,name = 'profile')
]
