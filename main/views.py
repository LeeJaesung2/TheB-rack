from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BycicleSerializer
from .models import Bycicle_info, Brack

# Create your views here.

def home(request):
    return render(request, 'home.html')


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
    serializer = BycicleSerializer(bycicle_info, data=request.data, partrial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #라즈베리 파이에서 값을 읽어가는 API // type확인용
# @api_view(['GET'])
# def get(request,bycicle_position):
#     bycicle_info = Bycicle_info.objects.get(pk = bycicle_position)
#     serializer = BycicleSerializer(bycicle_info)
#     return Response(serializer.data)

def rack(request,bycicle_position):
    brack = Brack()
    #brack.username = kakaousername
    brack.bycicle = get_object_or_404(Bycicle_info, pk=bycicle_position)
    brack.save()
    return redirect('home')