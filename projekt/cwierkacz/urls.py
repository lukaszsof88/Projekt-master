from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from .views import RegisterView, CustomLoginView
from cwierkacz.forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'cwierkacz'

urlpatterns = [
    # path('', views.HelloView.as_view(), name='hello'),
    path('', views.home, name='index'),
    path('rejestracja', RegisterView.as_view(), name='rejestracja'),
    path('logowanie', CustomLoginView.as_view(template_name='cwierkacz/signin.html'), name='logowanie'),
    path('wylogowanie', auth_views.LogoutView.as_view(template_name='cwierkacz/logout.html'), name='wylogowanie')
]
