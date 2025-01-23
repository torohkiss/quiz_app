from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from django.conf import settings
import datetime

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Get the last activity time from the session
            last_activity = request.session.get('last_activity')
            current_time = timezone.now()

            if last_activity:
                # Convert string to datetime if stored as string
                if isinstance(last_activity, str):
                    last_activity = datetime.datetime.fromisoformat(last_activity)
                
                # Check if session has expired (15 minutes)
                if (current_time - last_activity).seconds > 300:
                    logout(request)
                    return redirect('login')

            # Update last activity time
            request.session['last_activity'] = current_time.isoformat()

        response = self.get_response(request)
        return response
