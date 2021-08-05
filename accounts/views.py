from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import message, send_mail
from .serializer import UserSerializer
from user_profile.serializers import UserProfileSerializer

from django.contrib import auth
import requests
from random import randint
import random
import array


class Test(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({'success': 'test Passed.'})

class Signup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        email = data['email']
        password = data['password']
        re_password = data['re_password']
        mobile_no = data['mobile_no']
        first_name = data['first_name']
        last_name = data['last_name']
        try:
            if password == re_password:
                if User.objects.filter(email=email).exists() | UserProfile.objects.filter(mobile_no=mobile_no).exists():
                    return Response({"Error": "user Already Exists"})

                else:
                    if len(password) < 6:
                        return Response({'error': 'Password must be at least 6 characters'})
                    else:
                        user = User.objects.create_user(
                            username=email, password=password, email=email,)
                        user = User.objects.get(id=user.id)
                        useserializer = UserSerializer(user)
                        print(useserializer.data)
                        token = str(account_activation_token.make_token(user))
                        UserProfile.objects.create(
                            user=user, first_name=first_name, last_name=last_name, mobile_no=mobile_no, isemailverified=False)
                        current_site = str(get_current_site(request))
                        mail_subject = 'Activate your account.'
                        uuid = str(urlsafe_base64_encode(force_bytes(user.id)))
                        message = "To verify your account please click on link below\n" + \
                            "http://"+current_site+"/accounts/activate/"+uuid+"/"+token+"/"
                        send_mail(mail_subject, message, "justtrustyauth@gmail.com",
                                  [str(email)], fail_silently=True)
                        return Response({'success': 'Verification Mail Is Sent To Your Email Please Verify'})
            else:
                return Response({'error': 'Passwords do not match'})
        except Exception as e:
            return Response({'error': e})


class ActivateUser(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            print(uid)
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user_profile = UserProfile.objects.get(user_id=uid)
            user_profile.isemailverified = True
            user_profile.save()
            return Response('Thank you for your email confirmation. Now you can login your account.')
        else:
            return Response('Activation link is invalid!')


class ResetPassword(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = self.request.data
        email = data['email']
        user = User.objects.get(email=email)
        token = str(account_activation_token.make_token(user))
        current_site = str(get_current_site(request))
        mail_subject = 'Reset your account Password.'
        uuid = str(urlsafe_base64_encode(force_bytes(user.id)))
        message = "To Reset your account password please click on link below\n" + \
            "http://"+current_site+"/accounts/passwordreset/"+uuid+"/"+token+"/"
        send_mail(mail_subject, message, "justtrustyauth@gmail.com",
                  ["pankajkaule@gmail.com"], fail_silently=True)
        return Response({'success': 'mail is sent to your email please reset your password'})


class Updatepassword(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, uidb64, token):
        print(uidb64)
        try:
            data = self.request.data
            re_password = data['re_password']
            password = data['password']
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            if password == re_password:
                user.set_password(password)
                user.save()
                return Response('password reset successfully')
            return Response('Thank you for your email confirmation. Now you can login your account.')
        else:
            return Response('Activation link is invalid!')


class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        username = data['email']
        password = data['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                useserializer = UserSerializer(user)
                return Response({"data":useserializer.data})
            else:
                return Response({'error': 'Error Authenticating'})
        except Exception as e:
            return Response({'error': e+'Something went wrong when logging in'})


class SendOtp(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        data = self.request.data
        mobileno = data['mobileno']
        user_profile = UserProfile.objects.get(mobile_no=mobileno)
        randno = randint(100000, 999999)
        user_profile.otp = randno
        user_profile.save()
        url = "https://www.fast2sms.com/dev/bulkV2?authorization=qQP6Wym7RxnNacOfSVtUihdkH2bp4BYXFrwoIKD8uLTEMZ1esjYAEyVxegFSJv0jDMnOiaLmsGwc9qX7&route=v3&sender_id=TXTIND&message=Your%20Just%20Trusty%20Accont%20Verification%20code%20is%20{}&language=english&flash=0&numbers={}".format(
            randno, mobileno)
        response = requests.get(str(url))
        print()
        return Response({'success': response})


class Loginwithotp(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        mobileno = data['mobileno']
        otp = data['otp']
        if UserProfile.objects.filter(mobile_no=mobileno).exists():
            user11 = UserProfile.objects.filter(mobile_no=mobileno)
            customeraddressserializers = UserProfileSerializer(
                user11, many=True)
            databaseotp = customeraddressserializers.data[0]['otp']
            if databaseotp == otp:
                return Response({"success": "user Authenticated"})
            else:
                return Response({"error": "wrong credintials."})
        else:
            return Response({"user not exists"})


class GetUsersDetails(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request,pk):
        user = UserProfile.objects.get(id=pk)
        userdata=UserProfileSerializer(user)
        return Response({'data': userdata.data})