from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(CustomGO)
admin.site.register(Assignments)
admin.site.register(Data)