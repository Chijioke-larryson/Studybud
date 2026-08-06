# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q

from Insta.forms import RoomForm
from . models import Room,Topic

# Create your views here.


# rooms= [
#     {'id':1, 'name': 'Python'},
#     {'id':2, 'name': 'Django'}, 
#     {'id':3, 'name': 'JavaScript'},

# ]

def loginPage(request):
    context = {}

    return render(request, 'Insta/login_register.html', context)



def home(request):
   q = request.GET.get('q') if request.GET.get('q') != None else ''

   room = Room.objects.filter(
   Q(topic__name__icontains=q)|
   Q(name__icontains=q)|
   Q(description__icontains=q)
   )
   topics = Topic.objects.all()
   rooms_count = room.count()

   context = {'rooms': room, 'topics': topics, 'rooms_count': rooms_count}
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



def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    context = {'form' : form}
    return render(request, 'insta/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'insta/delete.html', {'obj': room})