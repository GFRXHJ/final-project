from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from . import template_views

urlpatterns = [
    # ==================== API Endpoints ====================
    
    # Authentication
    path('api/register/', views.register, name='api_register'),
    path('api/login/', views.login, name='api_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile Management
    path('api/profile/', views.get_profile, name='api_get_profile'),
    path('api/profile/update/', views.update_profile, name='api_update_profile'),
    path('api/change-password/', views.change_password, name='api_change_password'),
    
    # Password Recovery
    path('api/forgot-password/', views.forgot_password, name='api_forgot_password'),
    path('api/reset-password/', views.reset_password, name='api_reset_password'),
    
    # ==================== HTML Pages ====================
    path('', template_views.home_page, name='home'),
    path('docs/', template_views.docs_page, name='docs'),
    path('login/', template_views.login_page, name='login'),
    path('register/', template_views.register_page, name='register'),
    path('profile/', template_views.profile_page, name='profile'),
    path('forgot-password/', template_views.forgot_password_page, name='forgot_password'),
]