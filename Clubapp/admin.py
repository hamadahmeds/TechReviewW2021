from django.contrib import admin

from .models import Meeting, Meeting_Minutes, Resource ,Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Meeting_Minutes)
admin.site.register(Resource)
admin.site.register(Event)
