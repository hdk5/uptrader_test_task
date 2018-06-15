from django.shortcuts import render

# Create your views here.

def first_menu_view(request):
    return render(request, 'first_menu_view.html')
