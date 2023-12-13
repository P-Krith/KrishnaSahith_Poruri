from django.urls import path
from .views import (
    contact_list,
    contact_create,
    contact_update,
    contact_delete,
    contact_detail,
    contact_form,
)

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/<int:pk>/update/', contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', contact_delete, name='contact_delete'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/form/', contact_form, name='contact_form'),
    path('contacts/form/<int:pk>/', contact_form, name='contact_form'),
]
