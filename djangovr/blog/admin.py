#blog/admin.py
from django.contrib import admin
from .models import Request, Join


admin.site.register(Request)
admin.site.register(Join)
