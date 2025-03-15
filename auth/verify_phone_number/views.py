from django.shortcuts import redirect, render
from django.contrib import messages
from auth.views import AuthView
from django.contrib.auth.models import User
from django.contrib.auth import login
from auth.models import Profile

class VerifyPhoneOtpView(AuthView):
    template_name = 'auth/verify_otp.html'
    def get(self, request):
        # Render the login page for users who are not logged in.
        return super().get(request)

    def post(self, request):
        otp_entered = request.POST.get("otp")
        otp_stored = request.session.get("pending_user", {}).get("otp")

        if otp_entered == str(otp_stored):
            # OTP matched, proceed with user account creation
            user_data = request.session.get("pending_user")
            username = user_data["username"]
            email = user_data["email"]
            password = user_data["password"]
            phone_number = user_data["phone_number"]

            # Create the user
            created_user = User.objects.create_user(username=username, email=email, password=password)
            created_user.save()

            # Create user profile with phone number
            Profile.objects.create(user=created_user, phone_number=phone_number)

            # Log the user in
            login(request, created_user)

            # Clear session
            del request.session["pending_user"]

            messages.success(request, "Account created successfully!")
            return redirect("index")  # Redirect to home page
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect("verify-phone-otp")  # Redirect to OTP page for retry
