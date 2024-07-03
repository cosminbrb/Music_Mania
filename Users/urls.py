from django.urls import path
from django.contrib.auth import views as auth_views
from Users import views
from Users.views import CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomPasswordResetDoneView, \
    CustomPasswordResetView, CustomLogoutView

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('login/', auth_views.LoginView.as_view(form_class='AuthenticationNewForm'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path ('password_reset', CustomPasswordResetView.as_view (), name='password_reset'),
    path ('password_reset/done/', CustomPasswordResetDoneView.as_view (), name='password_reset_done'),
    path ('password_reset/complete/', CustomPasswordResetCompleteView.as_view (), name='password_reset_complete'),
    path ('password_reset_confirm/', CustomPasswordResetConfirmView.as_view (),
          name='password_reset_confirm'),
]