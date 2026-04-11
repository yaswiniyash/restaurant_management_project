from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import IsAuthenticated
from rest_framework import Response
from django.contrib.auth.models import User

from .serializers import UserUpdateSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def update(self, request):
        user = request.user

        serializer = UserUpdateSerializer(
            user,
            data=request.data,
            partial=False,
            context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "profile updated successfully", "data": serializer.data},status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)