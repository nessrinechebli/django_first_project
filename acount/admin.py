from django.contrib import admin
from .models import *
# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display=["profile_pic", "user","bio"]
    list_display_links=["user"]
    search_fields=["user"]
    list_filter=["user"]
    list_editable=["profile_pic"]
    ordering=["user","profile_pic"]


class CustomerAdmin(admin.ModelAdmin):
    list_display=["profile_pic", "user","status","preferences"]
    list_display_links=["user"]
    search_fields=["user"]
    list_editable=["profile_pic"]
    ordering=["user","profile_pic"]

admin.site.register(CustomerProfile,CustomerAdmin)
admin.site.register(AgentProfile, AgentAdmin)


