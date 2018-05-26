from django.contrib import admin

from graphql_app.models import Mod, AccessRecord, Webpage

# Register your models here.
admin.site.register(Mod)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
