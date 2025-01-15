from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from  .import views

urlpatterns = [
   path('',views.index, name='index'),
   path('signup/',views.signup, name='signup'),
   path('signout/',views.signout, name='signout'),
   path('signin', views.signin, name='signin'),
   path('trains', views.trainlist, name='trains'),
   path('search/', views.search_results, name='search'),
   path('book_ticket/', views.book_ticket, name='book_ticket'),
    path('booked/<str:p_name>/', views.booked, name='booking'),
   

   


  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)