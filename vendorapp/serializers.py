from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'  # You can specify the fields you want to include explicitly

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'  # Adjust this according to the fields you want to include

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'  # Modify this based on the fields you want to expose

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate', 'calculate_on_time_delivery_rate', 'calculate_quality_rating_avg', 'calculate_average_response_time', 'calculate_fulfillment_rate')

class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PurchaseOrder
        fields = [ 'acknowledgment_date']
        
