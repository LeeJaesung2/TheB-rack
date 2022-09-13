from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BycicleSerializer
from .models import Bycicle_info, Brack
from user.models import User
from thebrack import settings
import requests
from email.message import EmailMessage
import smtplib
import re


# Create your views here.

def home(request):
    brack = Brack()
    if request.user.username:
        user = request.user.username
        try:   
            brack = Brack.objects.get(username__username=user)
        except Brack.DoesNotExist:
            brack = Brack()
    return render(request, 'home.html',{'brack':brack})


#라즈베리에서 값을 보내주는 API
@api_view(['POST'])
def post(request):
    serializer = BycicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#라즈베리파이에서 status를 수정하는 API
@api_view(['PATCH'])
def update(request, bycicle_position):
    bycicle_info = Bycicle_info.objects.get(pk = bycicle_position)
    serializer = BycicleSerializer(bycicle_info, data=request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        brack = Brack.objects.get(pk=bycicle_position)
        brack.rack_time = timezone.now()
        try:
            brack.bycicle.status = 2
            brack.bycicle.save()
            data = {"position": brack.bycicle.position, "status": brack.bycicle.status, "rack_time": brack.bycicle.rack_time}
            sendMail(brack.username.email)
            return Response(data, status = status.HTTP_201_CREATED)
        except:
            brack.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #라즈베리 파이에서 값을 읽어가는 API // type확인용
# @api_view(['GET'])
# def get(request,bycicle_position):
#     bycicle_info = Bycicle_info.objects.get(pk = bycicle_position)
#     serializer = BycicleSerializer(bycicle_info)
#     return Response(serializer.data)

def rack(request,bycicle_position):
    try: 
        user = User.objects.get(username=request.user.username)
        try:
            brack = Brack.objects.get(pk = bycicle_position)
        except Brack.DoesNotExist:
            brack = Brack()
            brack.position = bycicle_position
            brack.username = user
            brack.bycicle = get_object_or_404(Bycicle_info, pk=bycicle_position)
            brack.bycicle.status = 1
            brack.bycicle.save()
            brack.save()
    except:
        return redirect('login')

    return redirect('home')

def remove(request):
    brack = Brack.objects.get(username__username=request.user.username)
    brack.bycicle.status = 0
    brack.bycicle.save()
    brack.delete()
    return redirect('home')

def email_is_valid(addr):
    if re.match('(^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,3}$)', addr):
        return True
    else:
        return False

def sendMail(mail):
    message = EmailMessage()
    message.set_content("자전거가 도난되었습니다")

    message["Subject"] = "자전거 상태 변경 알림"
    message["From"] = "dlwotjd9909@gmail.com"
    message["To"] = mail

    smtp = smtplib.SMTP_SSL(settings.SMTP_SERVER,settings.SMTP_PORT)
    smtp.login("dlwotjd9909@gmail.com","xthfcjxdabonlicn")

    email_is_valid(mail)
    if smtp.send_message(message)=={} :
        print("성공적으로 메일을 보냈습니다.")

    smtp.quit()



