from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',include("apps.bookmodule.urls")),
    path('user/',include("apps.usermodule.urls"))
]
