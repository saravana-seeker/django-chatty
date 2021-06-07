from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout',views.signout,name='signout'),
    path('contact/',views.contact,name='contact'),
   # path('page/',views.protected,name='protected'),
    path('custom/',views.customform,name='custom'),
    path('chat/', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]