from django.contrib import admin

from .models import Character
from .models import Traits

admin.site.register(Character)
admin.site.register(Traits)