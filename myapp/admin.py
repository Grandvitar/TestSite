from django.contrib import admin
from .models import SaveModel

@admin.register(SaveModel)
class SaveAdmin(admin.ModelAdmin):
    class Meta:
        db_table = 'first table'



