from django.contrib import admin
from .models import Logins, Worker


class LoginsAdmin(admin.ModelAdmin):
    list_display = ("id", "login", "password",)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "profession", "birth_date", "phone_number", "e_mail")


admin.site.register(Logins, LoginsAdmin)
admin.site.register(Worker, WorkerAdmin)
