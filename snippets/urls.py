from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]