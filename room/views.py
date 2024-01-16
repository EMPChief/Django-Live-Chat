from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room_obj = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room_obj).order_by('-date_added')[:25]
    return render(request, 'room/room.html', {
        'room': room_obj,
        'messages': messages,
        'room_slug': room_obj.slug
    })
