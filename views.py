from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.db import transaction



from django.template import loader
from .forms import AddStock_form
from .forms import register_form
from .forms import client_form
from .forms import InvoiceForm
from django.db.models import Q



from .models import Product
from .models import User_model
from .models import Client
from .models import Invoice

from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json




def home(request):
    return render(request,"home.html")

def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not password:
            messages.error(request, "Password is required")
            return redirect('account')

        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/dashboard')
            else:
                messages.error(request, "Incorrect password")
                return redirect('account')
        else:
            messages.error(request, "User does not exist")
            return redirect('account')
    else:
        return render(request, "account.html")

def logout_page(request):
    logout(request)
    return redirect('account')


    return render(request,"account")   


def register(request):
    if request.method == 'POST':
        fm=register_form(request.POST)
        if fm.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            hpw=make_password(password)   # hashing password

            user1=User.objects.filter(username=username)
            user2=User.objects.filter(email=email)
            if user1.exists():
                messages.info(request, "Username already exists!")
                return redirect('/register')
            elif user2.exists():
                messages.info(request, "email already exists!")
                return redirect('/register')

            #user creation adding to users(auth)
            user=User.objects.create(username=username,email=email,password=hpw)
            user.save()
            messages.success(request, "Register Successfully.")
            fm=register_form()
       
        return redirect('/account')

    else:
        fm=register_form()
    
    
    return render(request,"register.html",{'form':fm})


@login_required(login_url='/account')

def dashboard(request):
    
    return render(request,"dashboard.html") 

@login_required(login_url='/account')
def client(request):
    
    fm = client_form()  # Initialize fm with a default value

    if request.method == 'POST':
        fm = client_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/client')

    elif 'q' in request.GET:
        q = request.GET['q']
        all_clients = Client.objects.filter(client_name__icontains=q)  # Replace your_field_name with the actual field you want to search
        all_clients = Client.objects.filter(client_city__icontains=q) 
    else:
        all_clients = Client.objects.all()

    return render(request, "client.html", {'form': fm, 'CD': all_clients})

@login_required(login_url='/account')
def delete_client(request,id):    #delete Thaan from stock
    if request.method=='POST':
        pj=Client.objects.get(pk=id)
        pj.delete()
        return redirect('/client')

@login_required(login_url='/account')
def update_client(request,id): #update client or edit Thaans data

    if request.method =='POST':
        pi=Client.objects.get(pk=id)
        fm=client_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/client')
    else:
        pj=Client.objects.get(pk=id)
        fm=client_form(instance=pj)

    return render(request,"updateclient.html",{'form':fm})

@login_required(login_url='/account')
def AddStock(request):
    fm = AddStock_form()  # Initialize fm with a default value

    if request.method == 'POST':
        fm = AddStock_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/addstock')

    elif 'q' in request.GET:
        q = request.GET['q']
        all_Thaans = Product.objects.filter(name__icontains=q)  
    else:
        all_Thaans = Product.objects.all()

    # Pass the stock details to the billing form
    

    return render(request, "AddStock.html", {'form': fm, 'SD': all_Thaans})


@login_required(login_url='/account')
def delete_stock(request,id):    #delete Thaan from stock
    if request.method=='POST':
        pi=Product.objects.get(pk=id)
        pi.delete()
        return redirect('/addstock')

@login_required(login_url='/account')
def update_stock(request,id): #update Thaans or edit Thaans data

    if request.method =='POST':
        pi=Product.objects.get(pk=id)
        fm=AddStock_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/addstock')
    else:
        pi=Product.objects.get(pk=id)
        fm=AddStock_form(instance=pi)

    return render(request,"UpdateStock.html",{'form':fm})


@login_required(login_url='/account')
def get_client_details(request):
    client_id = request.GET.get('id', None)
    if client_id:
        client = Client.objects.get(id=client_id)
        # You can customize this response as per your client details
        data = {
            'name': client_name,
            'balance': client_balance,
            'phone': client_ph,
            # Add other fields as needed
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Client ID not provided'})


@login_required(login_url='/account')
def get_products(request):
    products = Product.objects.all().values('id', 'name')  # Fetch product data
    return JsonResponse(list(products), safe=False)




def invoice(request):
    stock_items = Product.objects.all()
    clients=Client.objects.all()
    return render(request, 'invoice.html', {'stock_items': stock_items,'clients':clients})


def get_rate(request, id):
    if request.method == 'GET':
        stock_item = Product.objects.get(pk=id)
        rate = stock_item.price
        return JsonResponse({'rate': rate})

def get_customer_details(request, id):
     if request.method == 'GET':
        customer = Client.objects.get(pk=id)
        phone = customer.phone
        city= customer.city
        balance=customer.balance
        return JsonResponse({'phone': phone,'city':city,'balance':balance})



def get_next_invoice_number(request):
    # Retrieve the next available invoice number
    last_invoice = Invoice.objects.order_by('-id').first()
    if last_invoice:
        last_invoice_number = int(last_invoice.invoice_number.split('INV')[-1])
        next_invoice_number = f"INV{last_invoice_number + 1:04d}"
    else:
        next_invoice_number = "INV0001"
    
    # Return the next available invoice number as JSON response
    return JsonResponse({'invoice_number': next_invoice_number})



#-----------------------------------------------------------------------------------------



@transaction.atomic
def save_invoice(request):
    if request.method == 'POST':
        # Extract invoice data from the request
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        total_amount = request.POST.get('total_amount')
        customer_id = request.POST.get('customerid')
        customer_name = request.POST.get('customer')
        stock_data_string = request.POST.get('stock_data', '[]')
        stock_data_list = json.loads(stock_data_string)

        print('stock_data_string',stock_data_string)
        print('stock_data_list',stock_data_list)

        # Create the invoice object
        invoice = Invoice(
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            total_amount=total_amount,
            customer=customer_name,
        )
        invoice.save()

        # Update customer's balance
        customer = Client.objects.get(pk=customer_id)
        customer.balance += float(total_amount)
        updated_balance = customer.balance
        customer.save()
        print('views updated balance',updated_balance)
        

        # Deduct quantity from stock
        try:
            for item_data in stock_data_list:
                item_id = int(item_data['stockId'])
                quantity = int(item_data['quantity'])
                stock_item = Product.objects.get(pk=item_id)
                print(f'Stock Item ID: {item_id}, Quantity: {quantity}')
                if stock_item.qty >= quantity:
                    stock_item.qty -= quantity
                    stock_item.save()
                else:
                    return JsonResponse({'error': f'Insufficient stock for item {stock_item.name}'}, status=400)
            return JsonResponse({'message': 'Invoice saved successfully', 'updated_balance': updated_balance}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'One or more products do not exist'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'success': False}, status=405)  # Method Not Allowed



#--------------------------------------------------------------------------------------
def view_invoices(request):
    q = request.GET.get('q')
    invoices = Invoice.objects.all()

    if q:
        # Split the query string by "-" to get start and end date
        date_range = q.split('-')
        if len(date_range) == 2:
            start_date_str, end_date_str = date_range
            try:
                # Parse the dates
                start_date = datetime.strptime(start_date_str.strip(), '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str.strip(), '%Y-%m-%d')
                # Filter invoices based on date range
                invoices = invoices.filter(invoice_date__range=[start_date, end_date])
            except ValueError:
                # Handle invalid date format
                pass
        else:
            # If date range is not provided, filter by other fields
            invoices = invoices.filter(
                Q(customer__icontains=q) |
                Q(invoice_date__icontains=q) |
                Q(total_amount__icontains=q) |
                Q(invoice_number__icontains=q)
            )

    return render(request, 'view_invoices.html', {'invoices': invoices})