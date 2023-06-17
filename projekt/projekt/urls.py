"""
URL configuration for projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cwierkacz import views
from cwierkacz.views import CustomLoginView, RegisterView
from django.contrib.auth import views as auth_views
from cwierkacz.forms import LoginForm
from cwierkacz.views import profile

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('cwierkacz.urls')),
  path('', views.home, name='index'),
  path('', include('posty.urls')),
  path('rejestracja', RegisterView.as_view(), name='rejestracja'),
  path('logowanie', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='cwierkacz/signin.html',
                                           authentication_form=LoginForm),  name='logowanie'),
  path('wylogowanie', auth_views.LogoutView.as_view(template_name='cwierkacz/logout.html'), name='wylogowanie'),
  path('profil/', profile, name='profil')
]
