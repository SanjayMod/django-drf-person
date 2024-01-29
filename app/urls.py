from django.urls import path
from app.views import (
    PersonCreateListView, 
    PersonDetailView
)


urlpatterns = [
    path('persons', PersonCreateListView.as_view(), name='person-create-list-view'),
    path('persons/<int:pk>', PersonDetailView.as_view(), name='person-detail-view')
]
