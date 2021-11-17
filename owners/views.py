from django.shortcuts import render


import json

from django.http     import JsonResponse
from django.views    import View

from .models import Owner, Dog

class Ownersview(View):
    def post(self, request):
        data     = json.loads(request.body)
        Owner.objects.create(
            name = data["name"],
            age = data["age"],
            email = data["email"]
        )


class Dogsview(View):
    def post(self, request):
        data     = json.loads(request.body)
        
        # print(f" a :: {a")
        Dog.objects.create(
            owner = Owner.objects.get(name=data["owner"]),
            name = data["name"],
            age = data["age"]
        )            

        # Owner.objects.create(name=data['name'])
        # Owner.objects.create(email=data['email'])
        # Owner.objects.create(age=data['age'])

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

# Create your views here.
