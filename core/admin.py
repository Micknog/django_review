from django.contrib import admin
from core.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'event_date', 'creation_date', 'user')
    list_filter = ('tittle',)


admin.site.register(Event, EventAdmin)
