from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')


def my_view(request):
    return render(request, 'my_template.html')

