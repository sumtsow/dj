from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
#from django.http import HttpResponse
from django.core.serializers import serialize

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

#Rest Api routes
def index_api(request):
    return render( request, 'api/index.html')

def groups_api(request):
    groups = Group.objects.all()
    data = serialize('json', groups)
    return JsonResponse(data, safe=False)

def subjects_api(request):
    subjects = Subject.objects.all()
    data = serialize('json', subjects)
    return JsonResponse(data, safe=False)

def cadets_api(request):
    cadets = Cadet.objects.all()
    cadets_str = serialize('json', cadets)
    template = {'container': '<div class="row"><div class="col"><h1>Курсанти</h1><table class="table table-striped"><thead><tr><th scope="col">Військове звання</th><th scope="col">Прізвище, ім&apos;я</th><th scope="col">Дата народження</th><th scope="col">Група</th></tr></thead><tbody>${ content }</tbody></table></div></div>', 'cadet': '<tr><td>${ cadet.rank.title }</td><td>${ cadet.lastname } ${ cadet.firstname }</td><td>${ cadet.birthdate }</td><td><a class="text-decoration-none" href="#">${ cadet.group.title }</a></td></tr>'}
    data = {'cadets': cadets_str, 'template': template}
    return JsonResponse(data, safe=False)