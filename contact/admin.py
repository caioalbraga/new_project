from django.contrib import admin

# Register your models here.
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ...