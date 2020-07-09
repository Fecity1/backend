from django.http import JsonResponse
from .models import Profile


# Представление пользователя
def get_profiles(request):

    profiles = []

    for p in Profile.objects.all():
        profiles.append({
            "name": p.name,
            "photo": p.photo.url
        })

    return JsonResponse({"profiles": profiles})


# Представление модели обращения
def get_Action(request):

    actions = []

    for a in Actions.objects.all():
        actions.append({
            "title": a.title,
            "date_init": a.date_init,
            "description": a.description,
        })
