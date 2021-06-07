from django.urls import path
from DoctorsPortal import views

urlpatterns = [
    path("", views.home, name="home"),
    path('checkSignin', views.checkSignin, name="checkSignin"),
    path('patientRegistration', views.patientRegistration, name="patientRegistration"),
    path('signUp', views.signUp, name="signUp"),  
    path('signin', views.signin, name="signin"),      
    path('addNewUserRegistration', views.addNewUserRegistration, name="addNewUserRegistration"),
    path('addNewPatientRegistration', views.addNewPatientRegistration, name="addNewPatientRegistration"),
    path('getAllPatientDetailsData', views.getAllPatientDetailsData, name="getAllPatientDetailsData"),
    path('logout', views.logout, name="logout"),


   
]

