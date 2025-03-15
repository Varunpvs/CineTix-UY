from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'screen', 'seat_number', 'booking_time', 'status')
    list_filter = ('status', 'booking_time')
    search_fields = ('user__username', 'screen__name', 'seat_number')
