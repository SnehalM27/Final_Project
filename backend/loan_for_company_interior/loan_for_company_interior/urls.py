
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from document_verification.views import BankViewSet, DocumentViewSet

from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('bank', BankViewSet, basename='bank')

router1 = DefaultRouter()
router1.register('doc',DocumentViewSet)


urlpatterns  = [
    path('admin/', admin.site.urls),
    path('bank/', include(router.urls)),
    path('doc/',include(router1.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)