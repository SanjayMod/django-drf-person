from django.urls import path
from app.views import PersonCreate


urlpatterns = [
    path('persons', PersonCreate.as_view(), name='person-create')
]
