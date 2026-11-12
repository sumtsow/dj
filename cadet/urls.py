from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='groups'),

    path('<int:group_id>/', views.group, name='group'),

#    path('group/<int:subject_id>/<int:group_id>/', views.group-subject, name='group-subject'),

    path('cadet/', views.cadets, name='cadets'),

    path('cadet/<int:cadet_id>/', views.cadet, name='cadet'),

    path('subject/', views.subjects, name='subjects'),

    path('subject/<int:group_id>/<int:subject_id>/', views.subject_group, name='subject_group'),

    path('subject/<int:subject_id>/', views.subject, name='subject'),
]
