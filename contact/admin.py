from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('listing','customer','contact_date','subject') #ðli ybanou godamou
    list_display_links=('listing','customer')# lien
    search_fields=('subject',)#bar de recherche
    list_filter=('contact_date',)

admin.site.register(Contact,ContactAdmin)