import json

from django.http     import JsonResponse
from django.views    import View

import owners

from .models import Owner, Dog

class Ownersview(View):
    def get(self, request):
        owners = Owner.objects.all()
        results  = []
        for owner in owners:
            ha = owner.dog_set.all() 
            dog_list = []
            for dog in ha:
                dog_list.append({
                    "name" : dog.name,
                    "age" : dog.age
                })
            results.append(
                {
                    "id"    : owner.id,
                    "name"  : owner.name,
                    "age"   : owner.age,
                    "email" : owner.email,
                    "dog_list" : dog_list
                }
            )

  
        
        return JsonResponse({"Result" : results}, status=200)

    def post(self, request):
        data     = json.loads(request.body)
        Owner.objects.create(
            name = data["name"],
            age = data["age"],
            email = data["email"]
        )
        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

class Dogsview(View):    
    def get(self, request):
        dogs = Dog.objects.all()
        results  = []
        for dog in dogs:
            results.append(
                {
                    "owner": dog.owner.name,
                    "name" : dog.name,
                    "age" : dog.age,
                }
            )
        
        return JsonResponse({"Result" : results}, status=200)
    
    def post(self, request):
        data = json.loads(request.body)
        """
        owner 이름
        """
        owner = Owner.objects.get(name=data['owner'])
        
        Dog.objects.create(
            owner = owner,
            name = data["name"],
            age = data["age"]
        )            

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

