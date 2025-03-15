from django.shortcuts import redirect
from django.contrib import messages
from auth.views import AuthView
from django.conf import settings
from twilio.rest import Client
import random

class RegisterView(AuthView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("index")  # Redirect logged-in users
        return super().get(request)  # Show registration form

    def post(self, request):
        print("came here")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        country_code = request.POST.get("country_code")
        phone_number = request.POST.get("phone_number")
        full_phone_number = f"{country_code}{phone_number}"

        # Generate a 6-digit OTP
        otp = random.randint(100000, 999999)

        # Store user details and OTP in the session (to create account later)
        request.session["pending_user"] = {
            "username": username,
            "email": email,
            "password": password,
            "phone_number": full_phone_number,
            "otp": otp
        }

        # Send OTP via Twilio
        try:
            # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            # client.messages.create(
            #     body=f"Your verification code is {otp}",
            #     from_=settings.TWILIO_PHONE_NUMBER,
            #     to=full_phone_number
            # )
            # messages.success(request, "OTP sent successfully.")
            print("OTP sent successfully.")
            return redirect("verify-phone-otp")  # Redirect to OTP verification page
        except Exception as e:
            messages.error(request, f"Failed to send OTP: {e}")
            return redirect("register")  # Redirect back to registration if there's an error
