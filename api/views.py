from rest_framework import status
from rest_framework.response import Response
from yaml import serialize
from rest_framework import permissions
from rest_framework import views

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import generics

from django.contrib.auth import login

from .models import Proje
from .serializers import ProjeSerializer, LoginSerializer, UserSerializer


class ProjeListCreateAPIView(APIView):
    
    def get(self,request):
        projeler = Proje.objects.all()
        serializer = ProjeSerializer(
            projeler,many=True,context={'request':request}
        )
        return Response(serializer.data)

    def post(request,self):
        serializer = ProjeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        

class ProjeDetailAPIView(APIView):
    
    def get_object(self, pk):
        proje_instance = get_object_or_404(Proje, pk=pk)
        return proje_instance

    def get(self, request, pk):
        proje = self.get_object(pk=pk)
        serializer = ProjeSerializer(proje) 
        return Response(serializer.data)       

    def put(self, request, pk):
        proje = self.get_object(pk=pk)
        serializer = ProjeSerializer(proje, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

    def delete(self, request, pk):
        proje = self.get_object(pk=pk)
        proje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
    

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
