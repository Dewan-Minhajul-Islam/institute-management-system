from django.urls import path
from users.views import *


urlpatterns = [
    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
]
