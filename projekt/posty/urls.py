from django.urls import path
from . import views
from posty.views import PostCreateView
from cwierkacz.views import profile

appapp_name = 'posty'

urlpatterns = [
    path('posty', views.list_of_post, name='posty'),
    path('posty/create', PostCreateView.as_view(), name='post_create'),
    path('wyszukaj/', views.BlogSearchView.as_view(), name='wyszukaj'),
    path('accounts/profile/', profile, name='profil'),
    path('posty/<slug:slug>', views.post_detail, name='post_detail'),
]