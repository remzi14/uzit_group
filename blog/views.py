from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import KursSerializers,Categoryserializers,MalimSerializers
from .models import Kurs,Category,Malim


class KurslistView(ListAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializers



class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers


class MalimListView(ListAPIView):
    queryset = Malim.objects.all()
    serializer_class = MalimSerializers


def home(request):
    return render(request,'index.html')



