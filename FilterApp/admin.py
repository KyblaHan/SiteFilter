from django.contrib import admin

# Register your models here.

from .models import InputImage, OutputImage

admin.site.register(InputImage)
admin.site.register(OutputImage)
