from django.shortcuts import render

from json import loads

from .models import Resume

def primaryResume(request, hashcode):
    resume = Resume.objects.get(hashcode = hashcode)
    data = loads(resume.data.replace("\'", "\""))
    return render(request, 'primary.html', {
        'data': data
    })