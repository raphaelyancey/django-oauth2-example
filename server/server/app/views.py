from django.shortcuts import render
from oauth2_provider.decorators import protected_resource
from django.http import HttpResponse
import json


@protected_resource(scopes=['read'])
def profile(request):
    return HttpResponse(json.dumps({
        "id": request.resource_owner.id,
        "username": request.resource_owner.username,
        "email": request.resource_owner.email,
        "first_name": request.resource_owner.first_name,
        "last_name": request.resource_owner.last_name
    }), content_type="application/json")
