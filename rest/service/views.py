from rest_framework import generics
from .model import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView, View
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import jsonpickle


# class UserAllView(generics.ListAPIView):
#     """
#     Provides a get method handler.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

from django.http import HttpResponse

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'birthday','address']


def retriveUsers(request):
    if request.method == 'GET':
        response={}
        users = User.objects.all()
        for user in users:
            data = model_to_dict(user)
            response.append(data)
        # print(users)
        # print(list(users))
        # data = serializers.serialize('json',users)
        # print(data)
        return JsonResponse(response, safe = False, status = 200)

def retriveUser(request,pk):
    if request.method == 'GET':
        user = User.objects.filter(id = pk).first()
        # print(user)
        # print(user.toJSON)
        # print(jsonpickle.encode(user))
        # data = serializers.serialize("json", user)
        # print(data)
        # data1 = serializers.serialize('json',[user,])
        # print(data1)
        data2 = model_to_dict(user)
        print(data2)
        return JsonResponse(data2, safe = False, status = 200)

def create(request):
    if request.method == 'POST':
        print(request.POST)
        # print(request.body) #correct
        # print(request.data)
        response={}
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            response['message']='created'
            return JsonResponse(response,status=201)
        response['message'] = 'error'
        return JsonResponse(response,status = 400)

def update(request,pk):
    if request.method == 'POST':
        response={}
        user,created = User.objects.update_or_create(
            id = pk,
            defaults={
                'name': request.POST['name'],
                'birthdady': request.POST['birthday'],
                'email': request.POST['email'],
                'address': request.POST['address'],
            }
        )
        if created:
            response['message']='updated'
            return JsonResponse(response,status = 202)

def delete(request, pk ):
    if request.method == 'GET':
        User.objects.filter(id = pk).delete()
        response = {}
        response['message']='deleted'
        return JsonResponse(response,status=200)
