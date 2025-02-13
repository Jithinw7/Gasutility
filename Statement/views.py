from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import ServiceRequest, Customer
from .serializers import ServiceRequestSerializer, CustomerSerializer

class CustomerAPIViews(GenericAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request):
        customers = self.queryset
        serializer = self.serializer_class(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceRequestAPIViews(GenericAPIView):
    serializer_class = ServiceRequestSerializer
    queryset = ServiceRequest.objects.all()

    def get(self, request):
        requests = self.queryset
        serializer = self.serializer_class(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceRequestRetrieveAPIViews(GenericAPIView):
    serializer_class = ServiceRequestSerializer
    queryset = ServiceRequest.objects.all()

    def get(self, request, pk):
        service_request = get_object_or_404(ServiceRequest, pk=pk)
        serializer = self.serializer_class(service_request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        service_request = get_object_or_404(ServiceRequest, pk=pk)
        serializer = self.serializer_class(service_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service_request = get_object_or_404(ServiceRequest, pk=pk)
        service_request.delete()
        return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
    