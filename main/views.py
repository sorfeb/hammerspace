from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Ballpoint pen',
        'amount ': '1',
        'description': 'Writing staple.'
    }

    return render(request, "main.html", context)