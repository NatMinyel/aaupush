from django.contrib import admin

from .models import Section, Lecturer, Material, Announcement, Folder
models = [Section, Lecturer, Material, Announcement, Folder]
for model in models:
    admin.site.register(model)
