from django.shortcuts import render, redirect, HttpResponse
from .models import Shows

def index(request):
    return render(request, 'index.html')

def register(request):
    print(request.POST)
    new_show = Shows.objects.create(title=request.POST['title'], network=request.POST['net'], release=request.POST['release'], description=request.POST['desc']) 
    request.session['title'] = request.POST['title']
    request.session['network'] = request.POST['net']
    request.session['release'] = request.POST['release']
    request.session['description'] = request.POST['desc']
    return redirect('/success')

def success(request):
    context = {
        'title' :request.session['title'],
        'net' :request.session['network'],
        'release' :request.session['release'],
        'desc' :request.session['description']
    }
    return render(request, 'new_shows.html', context)

def edit(request):
    return render(request, 'edit_shows.html')

def shows(request):
    print(request.POST)
    context = {
        "all_shows": Shows.objects.all(),
        # "new_title": Shows.objects.all(),
        # "new_network": Shows.objects.all(),
        # "new_release": Shows.objects.all(),
    }
    return render(request, 'all_shows.html', context)

def delete(request):
    request.session.flush()
    return redirect('/')

def add(request):
    return render(request, 'index.html')

def goto(request):
    return render(request, 'edit_shows.html')

def new(request):
    return render(request, 'new_shows.html')
    

# Create your views here.
