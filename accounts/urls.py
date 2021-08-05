from django.urls import path
from .views import Test,Signup,ActivateUser,GetUsersDetails,ResetPassword,Updatepassword,LoginView,SendOtp,Loginwithotp

urlpatterns = [
    path('', Test.as_view()),
    path('signup', Signup.as_view()),
    path('activate/<uidb64>/<token>/',ActivateUser.as_view()), 
    path('Resetpassword', ResetPassword.as_view()),
    path('passwordreset/<uidb64>/<token>/',Updatepassword.as_view()), 
    path('signin',LoginView.as_view()), 
    path('sendotp',SendOtp.as_view()), 
    path('otplogin',Loginwithotp.as_view()), 
    path('userdetails/<pk>',GetUsersDetails.as_view()), 


]
