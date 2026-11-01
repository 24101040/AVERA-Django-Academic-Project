from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def notification_list(request):
    notifications = request.user.notifications.all()

    return render(
        request,
        'notifications/list.html',
        {
            'notifications': notifications
        }
    )


from django.shortcuts import render

# Create your views here.
