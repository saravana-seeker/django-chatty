from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .forms import NewUserForm
from .models import Room, Message


def home(request):
    return render(request,'home.html')
    
def contact(request):
	return render(request, 'contact.html')



#Pa$$word@123
#P$$word@123
#santhosh Pass##1234

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			messages.success(request,"Registration successful")
			return redirect('home')
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, 'sign-up.html',{'signup':form})


def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,'sign-in.html',{'login_form':form})


def signout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("home")


def customform(request):
	return render(request,'404_page.html')

#chat

# Chat
@login_required
def chat(request):
	listof	=[]
	roomname = Room.objects.all()
	for names in roomname.iterator():
		listof.append(names.name)
	return render(request, 'chat.html',{'rooms':listof})

def room(request, room):
    username = request.user.get_username()
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
	room = request.POST['room_name']
	username = request.user.get_username()
	if Room.objects.filter(name=room).exists():
		return redirect('/'+room+'/?username='+username)
	else:
		new_room = Room.objects.create(name=room)
		new_room.save()
		return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.user.get_username()
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})








