from rest_framework.routers import SimpleRouter

from urls_app.views import URLCreateAPIView, URLCreateFreemiumAPIView

router = SimpleRouter()

router.register('urls', URLCreateFreemiumAPIView, basename='urls_free')

router.register('premium/urls', URLCreateAPIView, basename='urls_premium')

urlpatterns = [
    *router.urls
]
