from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from graphql_app.schema import schema

from graphene_django.views import GraphQLView


urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql = True, schema = schema)),
    #url(r'^$',views.index, name='index'),
]
