from django.http import JsonResponse
from .models import Profile


def get_profiles(request):

    profiles = []

    for p in Profile.objects.all():
        profiles.append({
            "name": p.name,
            "photo": p.photo.url
        })

    return JsonResponse({"profiles": profiles})
