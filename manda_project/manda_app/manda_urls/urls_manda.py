from django.urls import path
from ..manda_views import views_mandas

urlpatterns = [
    path('create/', views_mandas.manda_main_create, name='create'), 
    path('edit/sub/', views_mandas.update_manda_subs, name='edit_sub'),
]