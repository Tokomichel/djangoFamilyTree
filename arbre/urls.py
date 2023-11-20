from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('save', views.view),
    path('match', views.match),
    path('parent', views.parent),
    path('lis', views.liste),
    path('asce/<str:un>', views.ascendant, name='asce'),
    path('desce/<str:un>', views.descendant, name='desce')
]
