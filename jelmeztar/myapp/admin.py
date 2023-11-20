from django.contrib import admin
from .models import MyData

# Regisztráld a MyData modellt az admin felületen
admin.site.register(MyData)
