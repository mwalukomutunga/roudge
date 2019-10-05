from django.contrib import admin

from .models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'ticket_url', 'event_date', 'image')


admin.site.register(Events, EventsAdmin)
