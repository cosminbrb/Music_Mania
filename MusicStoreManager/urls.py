from django.urls import path
from MusicStoreManager import views

urlpatterns = [
    path('', views.HomeViewTemplate.as_view (), name='home'),
    path('albert/', views.AlbertViewTemplate.as_view (), name='albert'),
    path('bb/', views.BBViewTemplate.as_view(), name='bb'),
    path('beth/', views.BethViewTemplate.as_view(), name='beth'),
    path('buddy/', views.BuddyViewTemplate.as_view(), name='buddy'),
    path('christone/', views.ChristoneViewTemplate.as_view(), name='christone'),
    path('eric/', views.EricViewTemplate.as_view(), name='eric'),
    path('howtoplay/', views.HowToPlayViewTemplate.as_view(), name='howtoplay'),
    path('joe/', views.JoeViewTemplate.as_view(), name='joe'),
    path('srv/', views.SRVViewTemplate.as_view(), name='srv'),
    path('susan/', views.SusanViewTemplate.as_view (), name='susan'),

]