from django.urls import path,include
from users.views import getLoginView,getUserView,editUserView,createuserView


urlpatterns = [
    path('api/users/login',getLoginView),
    path('api/users/getuserlist',getUserView),
    path('api/users/edituserlist',editUserView),
    path('api/users/createuser',createuserView),



]
