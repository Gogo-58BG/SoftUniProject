from django.contrib import admin

from app.models import Traxxas


class TraxxasInline(admin.StackedInline):
    model = Traxxas


# class TraxxasAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'user')
#
#     inlines = (TraxxasInline,)


admin.site.register(Traxxas)


