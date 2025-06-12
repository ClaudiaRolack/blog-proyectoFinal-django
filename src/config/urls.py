from django.contrib import admin
from django.urls import path, include
from user.views import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
]
