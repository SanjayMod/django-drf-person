from django.urls import path
from app.views import PersonCreateListView


urlpatterns = [
    path('persons', PersonCreateListView.as_view(), name='person-create-list-view')
]
