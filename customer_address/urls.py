from django.urls import path
from .views import Test,AddUserAddress,getcustomersaddress

urlpatterns = [
    path('', Test.as_view()),
    path('addaddress/<pk>', AddUserAddress.as_view()),
    path('getcustomeraddress/<pk>', getcustomersaddress.as_view()),

]
