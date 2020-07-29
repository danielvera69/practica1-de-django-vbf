from .models import Contacto, Entrada
from django.contrib import admin


class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'modificacion']
    list_display = ('nombre', 'telefono', 'mail', 'creacion')
    ordering = ('nombre',)
    search_fields = ('nombre', 'mail')
    list_filter = ('nombre',)


admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Entrada)
