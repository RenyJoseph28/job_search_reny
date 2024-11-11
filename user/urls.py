from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signups', views.signups, name='signups'),
    path('login/', views.login, name='login'),
    #path('login_view',views.login_view,name='login_view'),
    path('dashboard/', views.dashboard, name='dashboard'),



    # Add other url patterns here
]
