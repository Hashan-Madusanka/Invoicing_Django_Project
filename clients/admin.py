from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "street_address", "city", "state", "email", "phone"]


admin.site.register(Client)
