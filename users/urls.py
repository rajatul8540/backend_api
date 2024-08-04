from django.urls import path,include
from users.views import getLoginView


urlpatterns = [
    path('api/login',getLoginView),
    # path('api/userlist',protected_view),

]
