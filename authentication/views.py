from django.db import IntegrityError
from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from api.models import Profile

from random import randint

@permission_classes((permissions.AllowAny,))
class UserExistsView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(data={
            	'exists': False
            })
        else:
            return Response(data={
            	'exists': True
            })

@permission_classes((permissions.AllowAny,))
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if Profile.objects.get(user = User.objects.get(username = username)).is_verified:
                return Response(data={
                    'status': 'success',
                    'is_verified': True
                })
            else:
                return Response(data={
                    'status': 'success',
                    'is_verified': False
                })
        else:
            return Response(data={
            	'status': 'error'
            })

@permission_classes((permissions.AllowAny,))
class SubmitOtpView(APIView):
    def post(self, request, *args, **kwargs):
        otp = request.data['otp']
        username = request.data['username']
        print(Profile.objects.get(user = User.objects.get(username = username)))
        registered_otp = Profile.objects.get(user = User.objects.get(username = username)).otp
        print(registered_otp)
        if otp == registered_otp:
            profile = Profile.objects.get(user = User.objects.get(username = username))
            profile.is_verified = True
            profile.save()
            return Response(data={'status': 'ok'})
        else:
            return Response(data={'status': 'error', 'message': 'Invalid OTP'})

@permission_classes((permissions.AllowAny,))
class ResendOtpView(APIView):
    def post(self, request, *args, **kwargs):
        otp = randint(100000, 999999)
        data = request.data
        username = data['username']
        emailid = data['emailid']
        profile = Profile.objects.get(user = User.objects.get(username = username))
        profile.otp = otp
        profile.save()
        message = Mail(
        from_email='adminn@markmycv.com',
        to_emails= emailid,
        subject='One Time Password for Mark My CV',
        html_content='<p>One Time Password to complete your registration at Mark My CV is {}</p>'.format(otp))
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response)
        except Exception as e:
            print('#####')
            print(e)
            print('#####')
        return Response({'status': 'success'})

@permission_classes((permissions.AllowAny,))
class ResendVOtpView(APIView):
    def post(self, request, *args, **kwargs):
        otp = randint(100000, 999999)
        data = request.data
        username = data['username']
        emailid = User.objects.get(username = username).email
        profile = Profile.objects.get(user = User.objects.get(username = username))
        profile.otp = otp
        profile.save()
        message = Mail(
        from_email='adminn@markmycv.com',
        to_emails= emailid,
        subject='One Time Password for Mark My CV',
        html_content='<p>One Time Password to complete your registration at Mark My CV is {}</p>'.format(otp))
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response)
        except Exception as e:
            print('#####')
            print(e)
            print('#####')
        return Response({'status': 'success'})

@permission_classes((permissions.AllowAny,))
class CreateAccountView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        fullname, username, emailid, password = data['fullname'], data['username'], data['emailid'], data['password']
        try:
            user = User.objects.get(email = emailid)
            return Response(data={ 'status': 'error', 'message': 'Email ID is already registered' })
        except User.DoesNotExist:
            print('Email ID is already registered')
        try:
            otp = randint(100000, 999999)
            user = User.objects.create_user(username, emailid, password)
            user.first_name, user.profile.otp = fullname, otp
            user.save()
            message = Mail(
            from_email='admin@markmycv.com',
            to_emails= emailid,
            subject='One Time Password for Mark My CV',
            html_content='<p>One Time Password to complete your registration at Mark My CV is {}</p>'.format(otp))
            try:
                sg = SendGridAPIClient('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')
                response = sg.send(message)
                print(response)
            except Exception as e:
                print('#####')
                print(e)
                print('#####')
            return Response(data={
            	'status': 'ok'
            })
        except IntegrityError:
            try:
                user = User.objects.get(email = emailid)
                email_registered = True
            except User.DoesNotExist:
                email_registered = False
            try:
                user = User.objects.get(username = username)
                username_registered = True
            except User.DoesNotExist:
                username_registered = False
            if email_registered and not username_registered:
                return Response(data={
                	'status': 'error',
                	'message': 'Email ID is already registered'
                })
            if username_registered and not email_registered:
                return Response(data={
                	'status': 'error',
                	'message': 'Username is already registered'
                })
            if username_registered and email_registered:
                return Response(data={
                	'status': 'error',
                	'message': 'Email ID and Username are already used'
                })
            return Response(data={
            	'status': 'error',
            	'message': 'Unknown error occoured, please report'
            })

@permission_classes((permissions.AllowAny,))
class ResetPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        value = request.data['value']
        try:
            user = User.objects.get(email = value)
            otp = randint(100000, 999999)
            user.profile.otp = otp
            user.save()
            message = Mail(
                from_email='admin@markmycv.com',
                to_emails= value,
                subject='One Time Password for Mark My CV',
                html_content='<p>One Time Password to complete your registration at Mark My CV is {}</p>'.format(otp)
            )
            return Response(data={
                'status': 'success',
                'message': "We've sent an OTP to Email ID jatinlal94@gmail.com. Please check your inbox and enter the OTP below. The OTP is a six digit integer, and is valid for 10 minutes only."
            })
        except User.DoesNotExist:
            pass
        try:
            user = User.objects.get(username = value)
            otp = randint(100000, 999999)
            user.profile.otp = otp
            user.save()
            """send_mail(
                'Confirmation Code for MarkMyCV',
                "OTP to reset your password is {}".format(otp),
                'admin@cryptopr.us',
                [value]
            )"""
            print(otp)
            return Response(data={
                'status': 'success',
                'message': "We've sent an OTP to Email ID j*********@gmail.com. Please check your inbox and enter the OTP below. The OTP is a six digit integer, and is valid for 10 minutes only."
            })
        except User.DoesNotExist:
            pass
        return Response(data={
            'status': 'error',
            'message': "No such user exists"
        })

@permission_classes((permissions.AllowAny,))
class ForgotOtpView(APIView):
    def post(self, request, *args, **kwargs):
        value = request.data['value']
        otp = request.data['otp']
        try:
            user = User.objects.get(email = value)
            if otp == user.profile.otp:
                return Response({
                    'status': 'success'
                })
            else:
                return Response({
                    'status': 'error',
                    'message': 'Incorrect OTP'
                })
        except User.DoesNotExist:
            pass
        try:
            user = User.objects.get(username = value)
            if otp == user.profile.otp:
                return Response({
                    'status': 'success',
                })
            else:
                return Response({
                    'status': 'error',
                    'message': 'Incorrect OTP'
                })
        except User.DoesNotExist:
            pass
        return Response(data={
            'status': 'error',
            'message': 'Username or Email ID not registered'
        })

@permission_classes((permissions.AllowAny,))
class NewPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        otp = request.data['otp']
        value = request.data['value']
        new_password = request.data['new_password']
        try:
            user = User.objects.get(email = value)
            if otp == user.profile.otp:
                user.set_password(new_password)
                user.save()
                return Response(data={
                    'status': 'success'
                })
            else:
                return Response(data={
                    'status': 'error',
                    'message': 'Incorrect OTP'
                })
        except User.DoesNotExist:
            pass
        try:
            user = User.objects.get(username = value)
            if otp == user.profile.otp:
                user.set_password(new_password)
                user.save()
                return Response(data={
                    'status': 'success'
                })
            else:
                return Response(data={
                    'status': 'error',
                    'message': 'Incorrect OTP'
                })
        except User.DoesNotExist:
            pass
        return Response(data={
            'status': 'success'
        })