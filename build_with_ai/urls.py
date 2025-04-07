"""
URL configuration for build_with_ai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from photos.views import (
    PhotoCreateView,
    PhotoDeleteView,
    PhotoListView,
    PhotoUpdateView,
)
from tags.views import TagListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PhotoListView.as_view(), name="photo-list"),
    path("photos/create", PhotoCreateView.as_view(), name="photo-create"),
    path("photos/<int:pk>/update", PhotoUpdateView.as_view(), name="photo-update"),
    path("photos/<int:pk>/delete", PhotoDeleteView.as_view(), name="photo-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
