from django.shortcuts import get_object_or_404, render

from .models import Character


def index(request):
    characters = Character.objects.all()
    context = {'characters': characters}
    return render(request, 'characters.html', context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'detail.html', {'character': character})