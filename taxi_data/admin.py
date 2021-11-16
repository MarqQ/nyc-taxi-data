from django.contrib import admin
from taxi_data.models import TaxiData


@admin.register(TaxiData)
class NycCabDataAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'vendor_id',
                    'tpep_pickup_datetime',
                    'tpep_dropoff_datetime',
                    'passenger_count',
                    'trip_distance',
                    'ratecode_id',
                    'store_and_fwd_flag',
                    'pulocation_id',
                    'dolocation_id',
                    'payment_type',
                    'fare_amount',
                    'extra',
                    'mta_tax',
                    'tip_amount',
                    'tolls_amount',
                    'improvement_surcharge',
                    'total_amount',
                    'congestion_surcharge')
