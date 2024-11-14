
# myportfolio/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Include the URLs from your main app
    #  path('', include('Blog.urls')),
    #  path('', include('Poems.urls')),
]
