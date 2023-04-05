from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import urllib.request
from api.models import Profile, Image
from generator.models import Resume

import random
import string

from json import loads, dumps
@permission_classes((permissions.AllowAny,))
class getProfile(APIView):
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user = User.objects.get(username = request.user.username))
        data = profile.data
        return Response(data={
            'data': data
        })

@permission_classes((permissions.AllowAny,))
class saveProfile(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data['data']
        profile = Profile.objects.get(user = User.objects.get(username = request.user.username))
        profile.data = request.data["data"]
        profile.save()
        return Response(data={
            'status': 'ok'
        })

def termsOfUse(request):
    file = open('content/terms-of-use.html', 'r+').read()
    return JsonResponse({
        'html': file
    })

def privacyPolicy(request):
    file = open('content/privacy-policy.html', 'r+').read()
    return JsonResponse({
        'html': file
    })

@permission_classes((permissions.AllowAny,))
class DownloadPrimaryResume(APIView):
    def post(self, request, *args, **kwargs):
        data = loads(dumps(request.data).replace("\'", "\""))["data"]
        hashcode = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])
        resume = Resume(
            user_id = User.objects.get(username = request.user),
            template_name = 'primary',
            data = dumps(data),
            hashcode = hashcode
        )
        resume.save()
        url = 'https://pdfgento.herokuapp.com/api/render?url=https://api.markmycv.com/generator/primary-resume/{}'.format(hashcode)
        urllib.request.urlretrieve(url, 'resumes/{}.pdf'.format(hashcode))
        return Response({'status': 'success', 'hashcode': hashcode})

@permission_classes((permissions.AllowAny,))
class UploadProfilePic(APIView):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        hashcode = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])
        image = Image(
            image = uploaded_file,
            hashcode = hashcode
        )
        image.save()
        return Response({
            'hashcode': hashcode
        })

@permission_classes((permissions.AllowAny,))
class UploadImage(APIView):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        hashcode = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])
        image = Image(
            image = uploaded_file,
            hashcode = hashcode
        )
        image.save()
        return Response({
            'hashcode': hashcode
        })

def picture(request, hashcode):
    image = Image.objects.get(hashcode = hashcode)
    print(settings.MEDIA_ROOT + '/' + image.image.name)
    with open(settings.MEDIA_ROOT + '/' + image.image.name, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
    response = HttpResponse(content_type="image/jpeg")