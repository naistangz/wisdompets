from django.contrib import admin

# importing our pet models

from .models import Pet


# registering class with the admin to tell it which model it is associated with using admin module Register
# creating a class that inherits from admin and overriding methods
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # This will allow us to define which fields are displayed on the listing screen in http://127.0.0.1:8000/admin/
    list_display = ['name', 'species', 'breed', 'age', 'sex']
