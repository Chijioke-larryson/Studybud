# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from Insta.forms import RoomForm
from . models import Room

# Create your views here.


rooms= [
    {'id':1, 'name': 'Python'},
    {'id':2, 'name': 'Django'}, 
    {'id':3, 'name': 'JavaScript'},

]
def home(request):
   room = Room.objects.all()
   context = {'rooms': rooms}
   return render(request,'Insta/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request,'Insta/room.html', context={'room': room})

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'Insta/room_form.html', context)

def comment(request):
    return HttpResponse("Let's Chat")