from django.contrib import admin
from django.urls import path , include
from account import views

urlpatterns = [

    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('account/',views.account,name='account'),  # account means login
    path('register/',views.register,name='register'),
    path('addstock/',views.AddStock,name='addstock'),
    path('delete/<int:id>/',views.delete_stock,name='deletestock'),
    path('update/<int:id>/',views.update_stock,name='updatestock'),
    path('logout/',views.logout_page,name='logout'),


]

