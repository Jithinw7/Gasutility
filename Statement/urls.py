from django.urls import path
from .views import CustomerAPIViews, ServiceRequestAPIViews, ServiceRequestRetrieveAPIViews  # Import views correctly

urlpatterns = [
    path('customers/', CustomerAPIViews.as_view(), name='customer-list-create'),
    path('requests/', ServiceRequestAPIViews.as_view(), name='service-request-list-create'),
    path('requests/<int:pk>/', ServiceRequestRetrieveAPIViews.as_view(), name='service-request-retrieve'),
]