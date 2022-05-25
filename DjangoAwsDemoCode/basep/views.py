from django.shortcuts import render
from .models import Wallpaper

# Create your views here.
def home(request):
    wallpapers = Wallpaper.objects.all()
    context = {
        "wallpaers": wallpapers,
    }
    
    return render(request, 'basep/index.html', context)