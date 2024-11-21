from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.work,name ="work"),
    path ("chat/" , views.chat,name ="chat"),

]