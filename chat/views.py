import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe


def index(request):
    print(request.resolver_match)
    return render(request, "chat/index.html")

# def room(request, room_name):
#     return render(request, "chat/room_boilterplate.html", {
#         "room_name": room_name
#     })


@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {
        "room_name_json": mark_safe(json.dumps(room_name)),
        "username": mark_safe(json.dumps(request.user.username)),
    })
