from django.contrib import admin

from .models import Group
from .models import Rank
from .models import Cadet

admin.site.register(Group)
admin.site.register(Rank)
admin.site.register(Cadet)
