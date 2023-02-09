from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    return HttpResponse("Rango says hey there partner! Link to about page: <a href='/rango/about/'>About</a>")
    
    # original code
    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page! Link to home page: <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_dict)