from django.contrib import admin

from .models import User, Vacation


class UserAdmin(admin.ModelAdmin):
    list_filter = ("username",)
    ordering = ("username",)


class VacationAdmin(admin.ModelAdmin):
    ordering = ("user",)


admin.site.register(User, UserAdmin)
admin.site.register(Vacation, VacationAdmin)
