from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from . models import movie

# Create your views here.
def home(request):
    Movie=movie.objects.all()
    context={
        'movie_list':Movie
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    Movies=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'Movies':Movies})

def add_movies(request):
    if request.method=='POST':
        name=request.POST.get('name')
        discription=request.POST.get('discription')
        year=request.POST.get('year')
        image=request.FILES['image']

        movies=movie(name=name,discription=discription,year=year,image=image)
        movies.save()

    return  render(request,'add.html')

def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES ,instance=Movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Movie':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
