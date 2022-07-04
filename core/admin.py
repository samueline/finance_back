from django.contrib import admin
from core.models.ingresos import Ingreso
from core.models.gastos import Gastos

from sqlite3 import adapt
from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin





# @admin.register(Ingreso)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','reputation','rides_taken','rides_offered')
#     search_fields = ('user__username','user__email','user__first_name','user__last_name')
#     list_filter = ('reputation',)


admin.site.register(Ingreso)
admin.site.register(Gastos)


