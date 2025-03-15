from django.contrib import admin
from .models import Poll

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('movie', 'yes_votes', 'threshold', 'decision')
    list_filter = ('decision',)
    search_fields = ('movie__title',)
