import models
from django.contrib import admin


class ShortURLAdmin(admin.ModelAdmin):
    pass


class WordAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ShortURL, ShortURLAdmin)
admin.site.register(models.Word, WordAdmin)