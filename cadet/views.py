from django.shortcuts import get_object_or_404, render

from .models import Group
from .models import Cadet

def index(request):
    return render( request, "groups/index.html", { "groups": Group.objects.all() })

def group(request, group_id):
    cadets = Cadet.objects.filter(group_id=group_id)
    #print(cadets)
    return render( request, "groups/group.html", { "cadets": cadets })

def cadets(request):
    return render( request, "cadets/index.html", { "cadets": Cadet.objects.all() })

def cadet(request, cadet_id):
    return render( request, "cadets/cadet.html", { "cadet": get_object_or_404(Cadet, pk=cadet_id) })
