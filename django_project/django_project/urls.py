from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from graphql_app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    path('', include('graphql_app.urls')),
]
