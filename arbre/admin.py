from django.contrib import admin
from .models import *


class PersoView(admin.ModelAdmin):
    list_display = ["id", "user_name", "sexe", "name", "last_name", "per", "mer"]

    def per(self, obj):
        pe = Personne.objects.get(id=obj.pere)
        if pe is None:
            return obj.pere
        else:
            return pe

    def mer(self, obj):
        me = Personne.objects.get(id=obj.mere)
        if me is None:
            return obj.mere
        else:
            return me

class PersoDbAdminView(admin.ModelAdmin):
    list_display = ["id", "user_name", "sexe", "name", "last_name", "pere", "mere"]
# Register your models here.

admin.site.register(Personne, PersoView)
# admin.site.register(Personne, PersoDbAdminView)
