from django.contrib import admin
# import your models here
from .models import Finch, Feeding

# Register your models here
admin.site.register(Finch)
admin.site.register(Feeding)