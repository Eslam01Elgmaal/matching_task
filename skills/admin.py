from django.contrib import admin
from .models import Skill, UserInput

# Register your models here.
admin.site.register(UserInput)
admin.site.register(Skill)