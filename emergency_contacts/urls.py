from django.urls import path
from .views import ContactCreateView, ContactDeleteView

urlpatterns = [
    path('api/contacts/', ContactCreateView.as_view(), name='create_contact'),
    path('api/contacts/<int:id>/', ContactDeleteView.as_view(), name='delete_contact'),
]
