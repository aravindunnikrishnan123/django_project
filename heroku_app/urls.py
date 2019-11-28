from django.urls import path
from . import views

urlpatterns = [
    path('',views.fn_myIndex),
    path('userlogin/',views.fn_userLogin),
    path('saveuserdata/',views.fn_saveUser),
    path('changepassword/',views.fn_updateUserPassword)
]