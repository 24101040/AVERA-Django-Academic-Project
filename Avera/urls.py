from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('adoption/', include('adoption.urls')),
    path('children/', include('children.urls')),
    path('feedback/', include('feedback.urls')),
    path('notifications/', include('notifications.urls')),
    path('organizations/', include('organizations.urls')),
    path('stories/', include('stories.urls')),
    path('support/', include('support.urls')),
    path('faq/', include('faq.urls')),
]

# Media URL
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)