from django.urls import path 

from . import views

urlpatterns = [
    path('',views.shopfasthome,name="shopfasthome"),
    
    path('nav/',views.navmaster,name="navmaster"),
    path('wishlist/',views.wishlist,name="wishlist"),
    path('offers/',views.offers,name="offers"),
    path('history/',views.history,name="history"),
    path('settings/',views.settings,name="settings"),
    path('contactus/',views.contactus,name="contactus"),
    path('feedback/',views.feedback,name="feedback"),
    path('aboutus/',views.aboutus,name="aboutus"),

]
