from django.shortcuts import render, get_object_or_404, redirect
from models import Announcement, Lecturer, Section, Folder, Material
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import authenticate, login
import datetime 

def section_view(request, section_code):
    section_object = get_object_or_404(Section, code=section_code)
  
    section_name = section_object.name
    now = datetime.datetime.now()
    section_announcements = section_object.announcement_set.order_by('-pub_date').filter(exp_date__gt=now)
    section_folders = section_object.folder_set.order_by('-last_update')
    this_week = []
    for folder in section_folders:
        a_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
        this_week.extend(folder.material_set.filter(pub_date__range=(a_week_ago, datetime.datetime.now()))) 
    this_week.sort(key=lambda mat: mat.pub_date) 
    this_week.reverse()
    context = {'name':section_name, 'code':section_code, 'announcements':section_announcements, 'folders':section_folders, 'this_week':this_week}

    return render(request, 'main/index.html', context)

def folder_view(request, section_code, folder_link_name):
    folder_name = folder_link_name.replace('-', ' ')
    folder_object = get_object_or_404(Folder, name=folder_name, section__code=section_code)

    folder_name = folder_object.name
    section_name = folder_object.section.name
    section_code = folder_object.section.code
    folder_materials = folder_object.material_set.order_by('-pub_date') 
    folder_last_update = folder_object.last_update

    context = {'name':folder_name, 'materials':folder_materials, 'section_name':section_name, 'section_code':section_code, 'last_update':folder_last_update}
    
    return render(request, 'main/folder.html', context)

def file_view(request, material_id):
    response = HttpResponse(content_type='application/pdf')
    material = get_object_or_404(Material, id=material_id)
    file_name = material.file.name.split('/')[-1]
    response['Content-Disposition'] = 'attachment; filename="%s"'%file_name
    response.write(material.file.read())
    return response

def login_view(request):
    if not request.POST:
        return render(request, 'main/login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('portal')
        else:
            message = 'Your account has been temporarily disabled. Please contact the web administrators at 0913350082.'
            return render(request, 'main/login.html', {'message':message})
    else:
        message = 'Invalid Username/Password.'
        return render(request, 'main/login.html', {'message':message})

def portal_view(request):
    if request.user.is_authenticated():
        user = request.user
        lecturer = get_object_or_404(Lecturer, user=user)
        folders = Folder.objects.filter(lecturer=lecturer)
        sections = set([folder.section for folder in folders])
        context = {'lecturer':lecturer, 'folders':folders, 'sections':sections}    
        return render(request, 'main/portal.html', context) 
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def backend_view(request):
    if not request.user.is_authenticated():
        return HttpResponseNotFound
    user = request.user
    type = request.POST.get('request_type')
    if type == 'announcement':
        message = request.POST.get('message')
        sections = [Section.objects.get(code=x) for x in request.POST.getlist('section')]
        by = Lecturer.objects.get(user=request.user)
        urgent = bool(request.POST.get('urgent'))
        pub_date = datetime.datetime.now()
        exp_date = pub_date + datetime.timedelta(days=int(request.POST.get('duration')))
        for section in sections:
            Announcement.objects.create(by=by, message=message, is_urgent=urgent, section=section, pub_date=pub_date, exp_date=exp_date)
        return redirect('portal')
    if type=='material':
        by = Lecturer.objects.get(user=user)
        name = request.POST.get('name')
        file = request.FILES.get('file_data')
        description = request.POST.get('description')
        folders = [Folder.objects.get(id=x) for x in request.POST.getlist('folder')]
        pub_date = datetime.datetime.now()
        for folder in folders:
            Material.objects.create(by=by, name=name, description=description, pub_date=pub_date, folder=folder, file=file)
        return redirect('portal') 

