from django.urls import path
from .views import ProjeListCreateAPIView,ProjeDetailAPIView,LoginView,ProfileView

urlpatterns=[
    path("projeler/", ProjeListCreateAPIView.as_view(), name="proje-listesi"),
    path('projeler/<int:pk>/', ProjeDetailAPIView.as_view(), name='proje-detay'),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),

]