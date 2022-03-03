from django.contrib import admin
from graphene_django.views import GraphQLView
from django.urls import path, include
from .schema import schema

urlpatterns = [
    # path('snippets/', include('snippets.urls', namespace='snippets')),
    path('graphql/', GraphQLView.as_view(
        graphiql=True,
        schema=schema
    )),
    path('admin/', admin.site.urls),
]
