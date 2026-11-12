from django.contrib import admin

from .models import Group
from .models import Rank
from .models import Cadet
from .models import Subject
from .models import Lesson
from .models import Mark

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'groups')

admin.site.register(Group)
admin.site.register(Rank)
admin.site.register(Cadet)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Mark)