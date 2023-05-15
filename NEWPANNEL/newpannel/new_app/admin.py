from django.contrib import admin
from .models import Developer
# Register your models here.
class developerAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "address")
    list_filter = ("image","name")
    search_fields = ('name__startswith',)
    fields = ('name','image', 'address')
    list_editable = ('image',)

admin.site.register(Developer, developerAdmin)
