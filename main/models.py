from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Lecturer(models.Model):
    user = models.ForeignKey(User)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name()
   
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

class Section(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.code

class Folder(models.Model):
    name = models.CharField(max_length=140)
    last_update = models.DateTimeField('Last Update')
    section = models.ForeignKey(Section)
    lecturer = models.ForeignKey(Lecturer)    

    def __str__(self):
        return '['+self.section.code+'] '+self.name

    def get_link_name(self):
        return self.name.replace(' ', '-')

class Announcement(models.Model):
    by = models.ForeignKey(Lecturer)
    message = models.CharField(max_length=140)
    is_urgent = models.BooleanField(default=False)
    section = models.ForeignKey(Section)
    pub_date = models.DateTimeField('Date Published')
    exp_date = models.DateTimeField('Expiry Date')

    def __str__(self):
        return self.message


def section_upload_path(instance, filename):
    return 'uploads/'+instance.folder.section.code+'/'+filename

class Material(models.Model):
    by = models.ForeignKey(Lecturer)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length = 140)
    pub_date = models.DateTimeField('Date Published')
    folder = models.ForeignKey(Folder)
    file = models.FileField(upload_to=section_upload_path)
    
    def __str__(self):
        return self.name

