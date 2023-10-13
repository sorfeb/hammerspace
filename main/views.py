from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum

#Login/Logout
from django.shortcuts import redirect
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#Cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

#Ajax
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    
    #Take all objects of Item from the current USER's database
    inventory = Item.objects.filter(user=request.user) 

    #Display number of items saved by USER
    total_amount = inventory.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'nama': request.user.username,
        'kelas': 'PBP-A',
        'aplikasi': 'hammerspace',
        'items': inventory,
        'items_counter' : total_amount,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "main.html", context)

def create_item(request):
    #Make new form
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    #Redirect after form data successfully saved
    return render(request, "create_item.html", context)
    
def show_xml(request): 
    #Store all Item(s) as data in xml
    data = Item.objects.all()
    #Translate object model to other format (its XML this time)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# def plus_item(request):
#     # Retrieve the Item instance based on the item_id
#     item = get_object_or_404(Item, pk=item_id)

#     # Call the plus_item method to increment the 'amount' field
#     item.plus_item()

#     return render(request, "create_item.html", context)

# def minus_item(request):
#     return render(request, "create_item.html", context)

# def delete_item(request):

#     return render(request, "create_item.html", context)

def edit_product(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def get_item_json(request):
    added_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', added_item))


@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()