from django.shortcuts import get_object_or_404, render

from .models import Group, Cadet, Subject, Lesson, Mark, Rank

# like var_dump()
# from inspect import getmembers
# from pprint import pprint

def index(request):
    return render( request, 'groups/index.html', { 'groups': Group.objects.all(), 'subjects': Subject.objects.all() })

def group(request, group_id):
    return render( request, 'groups/group.html', {'group': get_object_or_404(Group, pk=group_id), 'cadets': Cadet.objects.prefetch_related('rank').filter(group_id=group_id)  })

def cadets(request):
    return render( request, 'cadets/index.html', { 'cadets': Cadet.objects.prefetch_related('group', 'rank').all(), 'groups': Group.objects.all() })

def cadet(request, cadet_id):
    return render( request, 'cadets/cadet.html', { 'cadet': get_object_or_404(Cadet, pk=cadet_id) })

def subjects(request):
    return render( request, 'subjects/index.html', { 'subjects': Subject.objects.prefetch_related('groups').all() })

def subject(request, subject_id):
    return render( request, 'subjects/subject.html', { 'subject': Subject.objects.get(pk=subject_id), "lessons": Lesson.objects.filter(subject_id=subject_id) })

def subject_group(request, group_id, subject_id):
    cadets = Cadet.objects.prefetch_related('rank').filter(group_id=group_id)
    lessons = Lesson.objects.filter(subject_id=subject_id)
    marks = Mark.objects.filter(lesson_id__in=lessons, cadet_id__in=cadets)
    return render( request, 'subjects/subject_group.html', { 'subject': Subject.objects.get(pk=subject_id), "cadets": cadets, "lessons": lessons, "marks": marks })
