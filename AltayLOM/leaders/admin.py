from django.contrib import admin
from .models import Profile, Action


@admin.register(Profile)
class ImageAdmin(admin.ModelAdmin):
    """
    list_display = ('small_image_tag', 'image', 'tags')
    readonly_fields = ['medium_image_tag']  # обязательно read only режим
    fields = ('medium_image_tag', 'image', 'tags')
    """
@admin.register(Action)
class ImageAdmin(admin.ModelAdmin):
    pass
