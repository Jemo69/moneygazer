from django.urls import path ,include
from . import views
#urls are here
urlpatterns = [
    path("privacy",views.terms,name = "term"),
    path("terms",views.privacy,name = "privacy"),
    path("",views.home,name = 'home'),
    path("pricing", views.price,name = 'price' )
    
]
