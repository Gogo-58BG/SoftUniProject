from django.contrib import admin

from app.models import Traxxas


class TraxxasInline(admin.StackedInline):
    model = Traxxas


class TraxxasAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()

    inlines = (TraxxasInline,)


admin.site.register(Traxxas)


