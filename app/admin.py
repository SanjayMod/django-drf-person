from django.contrib import admin
from app.models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email'
    )


admin.site.register(Person, PersonAdmin)
