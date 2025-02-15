from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import PaymentViewSet
from orders.views import OrderViewSet
from menu.views import MenuViewSet
from feedback.views import FeedbackViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'menu', MenuViewSet)  # Corrected Menu ViewSet
router.register(r'feedback', FeedbackViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Single router for all endpoints
    path('api/auth/', include('rest_framework.urls')),  # Browsable API login
]
