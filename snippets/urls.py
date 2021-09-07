from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
] 

format_suffix_patterns(urlpatterns)
