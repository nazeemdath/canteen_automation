from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from payments.views import PaymentViewSet
from orders.views import OrderViewSet
from menu.views import MenuViewSet
from feedback.views import FeedbackViewSet
from users.views import UserViewSet, RegisterView, LoginView

# Creating a router and registering all viewsets
router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'users', UserViewSet)  # Handles /api/users/

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ JWT Authentication endpoints (JWT replaces session authentication)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ Custom login & register views
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),

    # ✅ Including all API routes from the router
    path('api/', include(router.urls)),
]
