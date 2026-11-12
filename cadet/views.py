from django.shortcuts import get_object_or_404, render

from .models import Group
from .models import Cadet
from .models import Subject


def index(request):
    return render( request, "groups/index.html", { "groups": Group.objects.all(), "subjects": Subject.objects.all() })

def group(request, group_id):
    return render( request, "groups/group.html", { "cadets": Cadet.objects.filter(group_id=group_id), "group": get_object_or_404(Group, pk=group_id), "subjects": Subject.objects.filter(groups__id=group_id) })

def cadets(request):
    return render( request, "cadets/index.html", { "cadets": Cadet.objects.all() })

def cadet(request, cadet_id):
    return render( request, "cadets/cadet.html", { "cadet": get_object_or_404(Cadet, pk=cadet_id) })

def subjects(request):
    return render( request, "subjects/index.html", { "subjects": Subject.objects.all() })

def subject(request, subject_id):
    return render( request, "subjects/subject.html", { "subject": get_object_or_404(Subject, pk=subject_id) })