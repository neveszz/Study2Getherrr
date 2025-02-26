from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.db.models import Q
from .models import Rooms, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password")  
    context = {'page':page}
    return render(request, 'login_register.html', context)

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'login_register.html', context={'form':form})

def logoutPage(request):
    logout(request)
    return redirect('home')

def home(request):
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    if search:
        rooms = Rooms.objects.filter(
            Q(topic__name__icontains=search) |
            Q(name__icontains=search) |
            Q(host__username__icontains=search)
            )
    else:
        rooms = Rooms.objects.all()
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=search)).order_by('-created')
    return render(request, "home.html", {'rooms':rooms, 'topics':topics, 'room_count':room_count, 'room_messages':room_messages})

def room(request, pk):
    room = Rooms.objects.get(pk=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user, body = request.POST.get('body'), room = room
            )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    return render(request, 'room.html', {'room':room,'room_messages':room_messages, 'participants':participants})

def userProfile(request, pk):
    perfil = True
    user = User.objects.get(pk=pk)
    rooms = user.rooms_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'user':user, 'rooms':rooms, 'room_messages':room_messages, 'topics':topics, 'room_count':room_count, 'perfil':perfil}
    return render(request,'profile.html', context)

def createRoom(request):
    form = RoomForm()  

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)  
            room.host = request.user
            room.save()  
            return redirect(reverse('home'))  

    context = {'form': form}
    return render(request, 'room_form.html', context=context)
    

def deleteRoom(request, pk):
    room = Rooms.objects.get(pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect(reverse('home'))
    else:
        return render(request, 'delete_room.html', {'room':room})
    

def updateRoom(request,pk):
    room = Rooms.objects.get(pk=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    context = {'form':form, 'room':room}
    return render(request, 'room_update.html', context=context)

@login_required(login_url="login")
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', pk=user.id)
    
    return render(request,'update_user.html', {'form':form})
