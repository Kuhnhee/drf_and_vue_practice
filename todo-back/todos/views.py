from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import TodoSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(status=400) #400 에러

# .../users/1/
@api_view(['GET'])
def user_detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    # 요청이 들어온 JWT의 user 정보와 pk로 검색하여 나온 user 객체의 정보가 같을 경우에만 허용해야한다.
    if request.user != user:
        return Response(status=404)

    serializer = UserSerializer(user)
    return Response(serializer.data)