from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # sub dir app name         #dir.urls
    path('my_app/', include('my_app.urls')),
]
