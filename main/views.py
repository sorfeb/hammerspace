from django.shortcuts import render

# Create your views here.
def show_main(request):
    items = [
    {   'name': 'Ballpoint pen',
        'amount ': '1',
        'description': 'Writing staple.'
    }
    ]
    
    context = {
        'items': items,
        'nama': 'Soros Febriano',
        'kelas': 'PBP-A',
        'aplikasi': 'hammerspace'
    }

    return render(request, "main.html", context, items)