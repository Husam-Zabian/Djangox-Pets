from django.contrib import admin

from .models import Pet

class CustomSnackAdmin(admin.ModelAdmin):
    model = Pet
    list_display = ['name', 'owner', 'desc',]
    fieldsets= (
        ('Owner',{
            'fields':('owner',
            )}
        ),
        ('Pet info',{
            'fields':('name','desc',
            )}
        )
    )

    
admin.site.register(Pet, CustomSnackAdmin)