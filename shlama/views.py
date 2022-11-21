from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import contact
from .serializer import ContactSerializer


# Create your views here.

class base1(View):
    def get(self, request):
        return render(request, 'shlama.html')

class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset =contact.objects.all()
    


