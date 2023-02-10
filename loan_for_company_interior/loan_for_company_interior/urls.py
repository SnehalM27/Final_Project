
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from document_verification.views import BankViewSet

router = DefaultRouter()
router.register('bank', BankViewSet, basename='bank')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bank/', include(router.urls))
]
