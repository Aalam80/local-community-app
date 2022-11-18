from unicodedata import name
from urllib import request
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .import views

urlpatterns = [
    
    path('',views.all_services,name='all_services'),
    path('',views.index, name='index'),
    path('add_service/',views.add_services,name='add_services'),
    path('About_Us/',views.About_Us,name='About_Us'),
    path('Contact_Us/',views.Contact_Us,name='Contact_Us'),
    path('services/',views.service,name='service'),
    path('serivce_detail<int:pk>/',views.service_detail,name='service_detail'),
    path('read/<int:pk>/',views.read, name='read'),
    path('Query/',views.Queris,name='Queris'),
    path('serQuery/',views.serQuery,name='serQuery'),
    path('register/',views.register_user,name='register_user'),
    # path('display_imgg/',views.display_imgg,name='display_imgg')
    # path('Replyform/',views.Replyform,name='Replyform')
    
    
   
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)