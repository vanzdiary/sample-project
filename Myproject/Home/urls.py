from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('about/',views.about,name='about'),
    path('show/',views.show,name='show'),
    path('Departments',views.Departments,name='Departments'),
    path('Doctors',views.Doctors,name='Doctors'),
    path('bookings',views.bookings,name='bookings'),
]