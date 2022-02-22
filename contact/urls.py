from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactsList.as_view(), name='contacts'),
    #path('<int:pk>/', views.ContactsDetailView.as_view(), name='contacts_detail'),
    # TODO: have a url slug for contacts
    path ('add-contact', views.AddContactView.as_view(), name='add_contact'),
]
