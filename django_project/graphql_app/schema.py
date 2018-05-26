from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType #NODE WILL INHERIT FROM THIS

from graphql_app.models import Mod

class ModNode(DjangoObjectType):
    class Meta:
        model = Mod
        interfaces = Node, #ModNode class is a Node

# how to detect information

class Query(ObjectType):
    mod = Node.Field(ModNode)
    all_mods = DjangoConnectionField(ModNode)

schema = Schema(query = Query)
