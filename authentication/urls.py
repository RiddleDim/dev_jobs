from django.urls import path
import authentication.views as a_views

urlpatterns = [
    path('login/', a_views.UserLogin.as_view(), name='login'),
    path('register/', a_views.Registration.as_view(), name='register'),
    path('logout/', a_views.user_logout, name='logout')
]
