from django.shortcuts import render
from django.urls import reverse


def index(request):
    print(request.resolver_match)
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room_boilterplate.html", {
        "room_name": room_name
    })
