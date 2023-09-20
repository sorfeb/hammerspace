from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum

# Create your views here.
def show_main(request):
    #Take all objects of Item from the database
    inventory = Item.objects.all() 

    #Display number of items saved
    total_amount = Item.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'nama': 'Soros Febriano',
        'kelas': 'PBP-A',
        'aplikasi': 'hammerspace',
        'items': inventory,
        'items_counter' : total_amount
    }
    return render(request, "main.html", context)

def create_item(request):
    #Make new form
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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


