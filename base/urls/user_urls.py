from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register_user, name='register_user'),
    path('profile/', views.get_user_profile, name='user_profile'),
    path('', views.get_users, name='users'),
]
