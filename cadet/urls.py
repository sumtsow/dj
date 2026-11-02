from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='groups'),

    path('<int:group_id>/', views.group, name='group'),

    path('cadet/', views.cadets, name='cadets'),

    path('cadet/<int:cadet_id>/', views.cadet, name='cadet'),
]
