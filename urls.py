from django.contrib import admin
from django.urls import path , include
from account import views

urlpatterns = [

    path('',views.account,name='account'),
    #path('home/',views.home,name='home'),
    path('account/',views.account,name='account'),  # account means login
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('client/',views.client,name='client'),
    path('addstock/',views.AddStock,name='addstock'),
    path('delete_stock/<int:id>/',views.delete_stock,name='deletestock'),
    path('update_stock/<int:id>/',views.update_stock,name='updatestock'),
    path('delete_client/<int:id>/',views.delete_client,name='deleteclient'),
    path('update_client/<int:id>/',views.update_client,name='updateclient'),
    path('logout/',views.logout_page,name='logout'),

    #testing urls
    path('get_client_details/', views.get_client_details, name='get_client_details'),
    path('invoice/',views.invoice,name='invoice'),
    path('get_rate/<int:id>/', views.get_rate, name='get_rate'),
    path('get_customer_details/<int:id>/', views.get_customer_details, name='get_customer_details'),
    path('get_next_invoice_number/', views.get_next_invoice_number, name='get_next_invoice_number'),
    path('save_invoice/', views.save_invoice, name='save_invoice'),
    path('view_invoices/', views.view_invoices, name='view_invoices'),

    


]

