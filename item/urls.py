
from django.urls import path
from item.views import detail,new

app_name = 'item'

urlpatterns = [
    path('<int:pk>', detail , name= 'detail'),
    path('new/', new , name='new')

] 

 