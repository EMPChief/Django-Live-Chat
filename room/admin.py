from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    readonly_fields = ['slug']

    def messages(self, obj):
        return ", ".join([message.content for message in obj.message_set.all()])

    messages.short_description = 'Messages'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
