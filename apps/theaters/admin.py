from django.contrib import admin
from .models import Theater, Screen


class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    ordering = ('name',)


class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'theater', 'total_rows', 'total_columns', 'movie', 'bookings_open')
    list_filter = ('theater', 'movie', 'bookings_open')
    search_fields = ('name', 'theater__name', 'movie__title')
    ordering = ('theater', 'name')
    actions = ['open_seat_booking']

    def open_seat_booking(self, request, queryset):
        """ Action to open seat booking for selected screens """
        for screen in queryset:
            try:
                screen.open_seat_booking()
                self.message_user(request, f"Bookings opened for {screen.name}.")
            except ValueError as e:
                self.message_user(request, f"Error opening bookings for {screen.name}: {str(e)}", level='error')

    open_seat_booking.short_description = "Open seat booking for selected screens"


admin.site.register(Theater, TheaterAdmin)
admin.site.register(Screen, ScreenAdmin)
